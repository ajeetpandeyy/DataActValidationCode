SELECT
	*
FROM award_financial
WHERE COALESCE(obligations_undelivered_or_fyb,0) <> COALESCE(ussgl480100_undelivered_or_fyb,0);