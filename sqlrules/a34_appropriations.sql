select * from appropriation as ap
    left JOIN sf_133 as sf ON ap.tas = sf.tas
    AND
        sf.period = 12 AND
        sf.fiscal_year = (ap.fiscal_year - 1)
WHERE sf.line = 2490 AND
    ap.budget_authority_unobligat_fyb <> sf.amount