SELECT *
FROM appropriation
left join sf_133 as sf
on appropriation.tas = sf.tas
where sf.line = 1910
and appropriation.budget_authority_available_cpe <> sf.amount