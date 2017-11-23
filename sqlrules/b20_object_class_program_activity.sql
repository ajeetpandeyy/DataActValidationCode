SELECT *
FROM award_financial AS af
WHERE  NOT EXISTS (
		SELECT 1
		FROM object_class_program_activity AS op
		WHERE (NOT (af.tas_with_sub <> op.tas_with_sub OR af.tas_with_sub IS NULL OR op.tas_with_sub IS NULL) OR (af.tas_with_sub IS NULL AND op.tas_with_sub IS NULL))
			AND ((NOT (af.program_activity_code <> op.program_activity_code OR af.program_activity_code IS NULL OR op.program_activity_code IS NULL) OR (af.program_activity_code IS NULL AND op.program_activity_code IS NULL))
				OR COALESCE(af.program_activity_code, '') = ''
				OR af.program_activity_code = '0000')
			AND ((NOT (af.object_class <> op.object_class OR af.object_class IS NULL OR op.object_class IS NULL) OR (af.object_class IS NULL AND op.object_class IS NULL))
				OR (af.object_class IN ('0', '00', '000', '0000')
					AND af.object_class IN ('0', '00', '000', '0000')
					)
				)
			AND af.period = op.period and af.fiscal_year = op.fiscal_year
	);