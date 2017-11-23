SELECT
	*
FROM object_class_program_activity
WHERE
	COALESCE(obligations_delivered_orde_fyb, 0) <> COALESCE(ussgl490100_delivered_orde_fyb, 0)