SELECT
	*
FROM award_financial
WHERE COALESCE(obligations_delivered_orde_cpe,0) <>
	COALESCE(ussgl490100_delivered_orde_cpe,0) +
	COALESCE(ussgl498100_upward_adjustm_cpe,0);