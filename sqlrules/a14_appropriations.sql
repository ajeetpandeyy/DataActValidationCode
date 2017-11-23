select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
WHERE sf.line = 3020 AND
    ap.gross_outlay_amount_by_tas_cpe <> sf.amount