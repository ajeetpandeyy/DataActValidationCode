SELECT *
FROM object_class_program_activity AS op
WHERE NOT EXISTS (
		SELECT 1
		FROM appropriation AS approp
		WHERE(NOT (op.tas_with_sub <> approp.tas_with_sub OR op.tas_with_sub IS NULL OR approp.tas_with_sub IS NULL) OR (op.tas_with_sub IS NULL AND approp.tas_with_sub IS NULL))
			AND op.fiscal_year = approp.fiscal_year and op.period = approp.period
	);
