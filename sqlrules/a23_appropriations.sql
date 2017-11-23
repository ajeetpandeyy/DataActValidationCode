select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
where sf.line = 2500 AND
    ap.status_of_budgetary_resour_cpe <> sf.amount