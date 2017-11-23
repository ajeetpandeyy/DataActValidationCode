select * from appropriation as ap
left join object_class_program_activity op on
ap.tas_with_sub = op.tas_with_sub and ap.period = op.period and ap.fiscal_year = op.fiscal_year
group by ap.tas_with_sub
having ap.deobligations_recoveries_r_cpe <>
        (SUM(op.ussgl487100_downward_adjus_cpe) +
        SUM(op.ussgl497100_downward_adjus_cpe) +
        SUM(op.ussgl487200_downward_adjus_cpe) +
        SUM(op.ussgl497200_downward_adjus_cpe))
