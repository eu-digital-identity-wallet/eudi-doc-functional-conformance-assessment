-- Improve dense ICS tables in the generated PDF.
--
-- The source Markdown tables are fine for MkDocs, but Pandoc gives pipe
-- tables equal column widths in LaTeX. For `# | ICS | value | EUDI-wallet`,
-- that leaves the narrow `#` column too wide and the descriptive ICS column
-- too narrow.

local stringify = pandoc.utils.stringify

local function header_texts(tbl)
  if not tbl.head or not tbl.head.rows or not tbl.head.rows[1] then
    return {}
  end

  local texts = {}
  for _, cell in ipairs(tbl.head.rows[1].cells) do
    texts[#texts + 1] = stringify(cell):lower()
  end
  return texts
end

local function is_ics_table(tbl)
  local headers = header_texts(tbl)
  return headers[1] == "#"
    and headers[2] == "ics"
    and headers[3] == "value"
    and headers[4] == "eudi-wallet"
end

function Table(tbl)
  if not is_ics_table(tbl) then
    return nil
  end

  tbl.colspecs = {
    { pandoc.AlignLeft, 0.06 },
    { pandoc.AlignLeft, 0.45 },
    { pandoc.AlignLeft, 0.22 },
    { pandoc.AlignLeft, 0.27 },
  }

  if FORMAT:match("latex") then
    return {
      pandoc.RawBlock("latex", "\\begingroup\\footnotesize\\setlength{\\tabcolsep}{3pt}\\renewcommand{\\arraystretch}{1.12}"),
      tbl,
      pandoc.RawBlock("latex", "\\endgroup"),
    }
  end

  return tbl
end
