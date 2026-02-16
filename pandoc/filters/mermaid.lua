-- pandoc/filters/mermaid.lua
-- Render ```mermaid``` code blocks to PNG via mermaid-cli (mmdc) for PDF output.
-- Compatible with Pandoc Lua (Lua 5.4) and os.execute() return semantics.

local stringify = pandoc.utils.stringify

-- ---------------------------
-- helpers
-- ---------------------------

local function mkdir_p(path)
  -- works on mac/linux runners
  os.execute(string.format('mkdir -p "%s"', path))
end

local function read_file(path)
  local f = io.open(path, "rb")
  if not f then return nil end
  local s = f:read("*a")
  f:close()
  return s
end

local function write_file(path, content)
  local f = assert(io.open(path, "wb"))
  f:write(content)
  f:close()
end

local function trim(s)
  return (s:gsub("^%s+", ""):gsub("%s+$", ""))
end

local function join_path(a, b)
  if a:sub(-1) == "/" then return a .. b end
  return a .. "/" .. b
end

local function file_exists(path)
  local f = io.open(path, "rb")
  if f then f:close(); return true end
  return false
end

-- robust success detection for Lua 5.2+ / 5.4
local function run_cmd(cmd, logfile)
  local full = cmd
  if logfile and logfile ~= "" then
    full = cmd .. string.format(' >"%s" 2>&1', logfile)
  end

  local a, b, c = os.execute(full)

  -- Lua 5.1: returns status code (number)
  if type(a) == "number" then
    return (a == 0), a
  end

  -- Lua 5.2+: returns (true/nil), "exit"/"signal", code
  if type(a) == "boolean" then
    if a == true then
      return true, 0
    end
    -- a == nil means failure
    return false, tonumber(c) or 1
  end

  -- fallback
  return false, 1
end

local function sha1_hex(s)
  -- use openssl if available, else shasum
  -- (works on ubuntu + mac typically)
  local tmp = os.tmpname()
  write_file(tmp, s)

  local cmd1 = string.format('openssl sha1 "%s" 2>/dev/null | awk \'{print $2}\'', tmp)
  local p1 = io.popen(cmd1)
  local out1 = p1 and p1:read("*a") or ""
  if p1 then p1:close() end
  out1 = trim(out1)

  if out1 == "" then
    local cmd2 = string.format('shasum -a 1 "%s" 2>/dev/null | awk \'{print $1}\'', tmp)
    local p2 = io.popen(cmd2)
    local out2 = p2 and p2:read("*a") or ""
    if p2 then p2:close() end
    out1 = trim(out2)
  end

  os.remove(tmp)
  return out1 ~= "" and out1 or tostring(math.random(1, 10^12))
end

-- ---------------------------
-- config
-- ---------------------------

local OUTDIR = "build/mermaid"
local MMDC   = "mmdc"
local CONFIG = "pandoc/mermaid-config.json"

-- Render size defaults (tune as you like)
local WIDTH  = "1800"
local SCALE  = "2"
local BGCOLOR = "white"

-- ---------------------------
-- render
-- ---------------------------

local function render_mermaid_png(mermaid_src)
  mkdir_p(OUTDIR)

  local cfg = read_file(CONFIG) or ""
  local key = sha1_hex(mermaid_src .. "\n---\n" .. cfg)

  local in_mmd = join_path(OUTDIR, key .. ".mmd")
  local out_png = join_path(OUTDIR, key .. ".png")
  local log = join_path(OUTDIR, key .. ".log")

  if not file_exists(out_png) then
    write_file(in_mmd, mermaid_src)

    local cmd = string.format(
      '%s -i "%s" -o "%s" -b %s -c "%s" -w %s -s %s',
      MMDC, in_mmd, out_png, BGCOLOR, CONFIG, WIDTH, SCALE
    )

    local ok, rc = run_cmd(cmd, log)
    if not ok or not file_exists(out_png) then
      io.stderr:write("Mermaid rendering failed.\n")
      io.stderr:write("Command: " .. cmd .. "\n")
      io.stderr:write("Exit code: " .. tostring(rc) .. "\n")
      local l = read_file(log)
      if l and l ~= "" then
        io.stderr:write("---- mmdc log ----\n")
        io.stderr:write(l .. "\n")
        io.stderr:write("---- end log ----\n")
      end
      return nil
    end
  end

  return out_png
end

-- ---------------------------
-- Pandoc filter entry point
-- ---------------------------

function CodeBlock(cb)
  local classes = cb.classes or {}
  local is_mermaid = false
  for _, c in ipairs(classes) do
    if c == "mermaid" then is_mermaid = true end
  end

  -- also allow ```{.mermaid}``` or ```mermaid``` style
  if not is_mermaid then
    if cb.attr and cb.attr.classes then
      for _, c in ipairs(cb.attr.classes) do
        if c == "mermaid" then is_mermaid = true end
      end
    end
  end

  if not is_mermaid then
    return nil
  end

  local src = cb.text or ""
  local png = render_mermaid_png(src)

  if not png then
    -- keep the code block so you can see the source in the PDF if rendering fails
    return cb
  end

  -- Use a figure-like block so it behaves nicely in PDFs
  local caption = ""
  if cb.attr and cb.attr.attributes and cb.attr.attributes.caption then
    caption = cb.attr.attributes.caption
  end

  local img = pandoc.Image(caption, png)
  img.attr = img.attr or pandoc.Attr()
  img.attr.attributes = img.attr.attributes or {}
  img.attr.attributes["width"] = "100%"  

  return pandoc.Para({ img })
end
