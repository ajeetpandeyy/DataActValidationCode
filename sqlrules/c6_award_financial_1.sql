SELECT
	*
FROM award_financial
WHERE COALESCE(gross_outlays_undelivered_cpe,0) <>
	COALESCE(ussgl480200_undelivered_or_cpe,0) +
	COALESCE(ussgl488200_upward_adjustm_cpe,0);