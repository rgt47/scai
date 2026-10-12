-- Rewrite cross-references that point into the other print volume.
--
-- Each print profile renders only its own chapters, so a reference
-- such as @sec-simulation from Volume II has no target and Quarto
-- would print '?@sec-simulation'. This filter runs before Quarto's
-- cross-reference pass and replaces such a reference with plain text,
-- 'Volume I, Chapter 8'. A label below chapter level (a section or a
-- table) is reported by its chapter only.
--
-- Chapter numbers come from _quarto-html.yml, the full book, so they
-- agree with the website and with Volume II's counter offset. Volume
-- membership comes from _quarto-vol1.yml; every other numbered chapter
-- is in Volume II. The filter is a no-op unless the profile sets
-- 'volume' in its metadata.

local ROMAN = { 'I', 'II' }
local LABEL_PREFIXES = { sec = true, fig = true, tbl = true, eq = true }

local function project_dir()
  if quarto and quarto.project and quarto.project.directory then
    return quarto.project.directory
  end
  return '.'
end

local function read_lines(path)
  local f = io.open(path, 'r')
  if not f then
    error('cross-volume.lua: cannot read ' .. path)
  end
  local lines = {}
  for line in f:lines() do
    lines[#lines + 1] = line
  end
  f:close()
  return lines
end

local function chapter_files(config_path)
  local files = {}
  for _, line in ipairs(read_lines(config_path)) do
    local name = line:match('^%s*%-%s*([%w%-_]+%.qmd)%s*$')
    if name then
      files[#files + 1] = name
    end
  end
  return files
end

local function is_unnumbered(lines)
  for _, line in ipairs(lines) do
    if line:match('^# ') then
      return line:match('%.unnumbered') ~= nil or line:match('{%-}') ~= nil
    end
  end
  return true
end

local function build_label_map()
  local dir = project_dir()
  local in_vol1 = {}
  for _, name in ipairs(chapter_files(dir .. '/_quarto-vol1.yml')) do
    in_vol1[name] = true
  end

  local map = {}
  local chapter = 0
  for _, name in ipairs(chapter_files(dir .. '/_quarto-html.yml')) do
    local lines = read_lines(dir .. '/' .. name)
    if not is_unnumbered(lines) then
      chapter = chapter + 1
      local volume = in_vol1[name] and 1 or 2
      for _, line in ipairs(lines) do
        for label in line:gmatch('{#([%a]+%-[%w_%-]+)') do
          local prefix = label:match('^(%a+)%-')
          if LABEL_PREFIXES[prefix] then
            map[label] = { volume = volume, chapter = chapter }
          end
        end
      end
    end
  end
  return map
end

local current_volume = nil
local label_map = nil

local function read_volume(meta)
  if meta.volume ~= nil then
    current_volume = tonumber(pandoc.utils.stringify(meta.volume))
  end
end

local function rewrite_cite(cite)
  if current_volume == nil then
    return nil
  end
  label_map = label_map or build_label_map()

  local out = pandoc.Inlines({})
  local changed = false
  for i, citation in ipairs(cite.citations) do
    local target = label_map[citation.id]
    if i > 1 then
      out:insert(pandoc.Str(';'))
      out:insert(pandoc.Space())
    end
    if target and target.volume ~= current_volume then
      changed = true
      out:insert(pandoc.Str(
        'Volume ' .. ROMAN[target.volume] .. ', Chapter ' .. target.chapter
      ))
    else
      out:insert(pandoc.Cite(pandoc.Inlines({ pandoc.Str('@' .. citation.id) }),
        { citation }))
    end
  end
  if changed then
    return out
  end
  return nil
end

return {
  { Meta = read_volume },
  { Cite = rewrite_cite },
}
