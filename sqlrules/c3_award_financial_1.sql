SELECT
	*
FROM award_financial
WHERE
COALESCE(obligations_undelivered_or_cpe,0) <>
	COALESCE(ussgl480100_undelivered_or_cpe,0) +
	COALESCE(ussgl488100_upward_adjustm_cpe,0);