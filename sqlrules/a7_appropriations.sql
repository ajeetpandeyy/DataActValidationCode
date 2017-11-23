
SELECT *
FROM appropriation as approp
left join sf_133 as sf
on approp.tas = sf.tas
and approp.period = sf.period
and approp.fiscal_year = sf.fiscal_year
WHERE sf.line = 1000 AND
    approp.budget_authority_unobligat_fyb <> sf.amount