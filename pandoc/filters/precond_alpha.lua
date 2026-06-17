-- pandoc/filters/precond_alpha.lua
-- Render the ordered list under each "Preconditions" heading with uppercase
-- alphabetic markers (A., B., C., ...) in the PDF, to match the website, where
-- the same effect is produced with CSS (list-style-type: upper-alpha).
--
-- Preconditions are authored as a normal numbered Markdown list (1., 2., 3., ...)
-- so the raw Markdown stays clean and the list renders correctly everywhere; this
-- filter only changes the *marker style* of that one list. Every other ordered
-- list (Test Scenario, Expected results) is left numeric.

local stringify = pandoc.utils.stringify

function Pandoc(doc)
  local expect = false
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      -- the next ordered list belongs to Preconditions only if this is its heading
      expect = (stringify(b):lower() == "preconditions")
    elseif b.t == "RawBlock" then
      -- include-markdown comment markers may sit between heading and list; skip them
    elseif b.t == "OrderedList" then
      if expect then
        b.listAttributes.style = "UpperAlpha"
      end
      expect = false
    else
      expect = false
    end
  end
  return doc
end
