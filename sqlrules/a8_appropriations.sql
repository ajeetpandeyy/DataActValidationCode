select *
from appropriation as approp
left join sf_133 as sf
on approp.tas = sf.tas and approp.period = sf.period and approp.fiscal_year = sf.fiscal_year
where sf.line in (1160, 1180, 1260, 1280)
group by approp.tas
having approp.budget_authority_appropria_cpe != sum(sf.amount)