select * from appropriation as ap
left join sf_133 as sf
on ap.tas = sf.tas and ap.fiscal_year = sf.fiscal_year and ap.period = sf.period
where sf.line in (1540, 1640)
group by ap.tas
having ap.contract_authority_amount_cpe <> SUM(sf.amount)
