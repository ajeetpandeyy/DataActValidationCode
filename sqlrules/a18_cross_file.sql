SELECT * FROM appropriation as ap
left join object_class_program_activity as op
on ap.tas_with_sub = op.tas_with_sub and ap.fiscal_year = op.fiscal_year and ap.period = op.period
group by ap.tas_with_sub
having ap.gross_outlay_amount_by_tas_cpe <> SUM(op.gross_outlay_amount_by_pro_cpe)
