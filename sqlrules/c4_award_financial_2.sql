SELECT
	*
FROM award_financial
WHERE COALESCE(obligations_delivered_orde_fyb,0) <>
	COALESCE(ussgl490100_delivered_orde_fyb,0);