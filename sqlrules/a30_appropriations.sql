select * from appropriation as ap
where not exists (select 1 from object_class_program_activity as op
where (NOT (ap.tas_with_sub <> op.tas_with_sub OR ap.tas_with_sub IS NULL OR op.tas_with_sub IS NULL) OR (ap.tas_with_sub IS NULL AND op.tas_with_sub IS NULL)) and
ap.period = op.period and ap.fiscal_year = op.fiscal_year);
