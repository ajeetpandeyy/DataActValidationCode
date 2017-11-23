SELECT
	*
FROM object_class_program_activity
WHERE
	COALESCE(obligations_undelivered_or_cpe, 0) <>
	    (COALESCE(ussgl480100_undelivered_or_cpe, 0) +
		COALESCE(ussgl488100_upward_adjustm_cpe, 0))