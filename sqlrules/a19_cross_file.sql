select * FROM appropriation AS ap
	left JOIN object_class_program_activity op
		ON ap.tas_with_sub = op.tas_with_sub
			AND ap.period = op.period and ap.fiscal_year = op.fiscal_year
GROUP BY ap.tas_with_sub
HAVING ap.obligations_incurred_total_cpe <> SUM(op.obligations_incurred_by_pr_cpe) * -1