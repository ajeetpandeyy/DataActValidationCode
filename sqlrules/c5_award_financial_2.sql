SELECT
	*
FROM award_financial
WHERE COALESCE(gross_outlay_amount_by_awa_fyb,0) <>
	COALESCE(gross_outlays_undelivered_fyb,0) +
	COALESCE(gross_outlays_delivered_or_fyb,0);