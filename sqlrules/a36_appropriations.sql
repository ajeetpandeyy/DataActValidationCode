select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
WHERE sf.line = 1000 AND
    sf.amount <> 0 AND
    ap.budget_authority_unobligat_fyb == 0