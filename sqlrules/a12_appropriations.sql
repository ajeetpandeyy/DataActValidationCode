select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
WHERE (sf.line >= 1010 AND sf.line <= 1042)
GROUP BY ap.tas
HAVING ap.adjustments_to_unobligated_cpe <> SUM(sf.amount)