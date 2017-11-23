SELECT
	*
FROM object_class_program_activity
WHERE
	COALESCE(obligations_undelivered_or_fyb, 0) <> COALESCE(ussgl480100_undelivered_or_fyb, 0)