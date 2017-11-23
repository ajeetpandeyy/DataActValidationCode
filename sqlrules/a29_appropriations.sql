select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
where sf.line in (1021, 1033)
GROUP BY ap.tas
HAVING ap.deobligations_recoveries_r_cpe <> SUM(sf.amount)