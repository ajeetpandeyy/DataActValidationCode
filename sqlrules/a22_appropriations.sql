select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
where sf.line = 2190 AND
    ap.obligations_incurred_total_cpe <> sf.amount