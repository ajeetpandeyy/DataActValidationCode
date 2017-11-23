SELECT
	*
FROM object_class_program_activity
WHERE
	COALESCE(obligations_delivered_orde_cpe, 0) <>
	    (COALESCE(ussgl490100_delivered_orde_cpe, 0) +
		COALESCE(ussgl498100_upward_adjustm_cpe, 0))