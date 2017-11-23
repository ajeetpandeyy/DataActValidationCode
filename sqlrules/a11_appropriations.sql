select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
where sf.line in (1750, 1850)
group by ap.tas
having ap.spending_authority_from_of_cpe <> SUM(sf.amount)


