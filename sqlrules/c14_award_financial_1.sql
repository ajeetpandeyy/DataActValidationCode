SELECT *
FROM award_financial
WHERE (fain IS NULL or fain is 0)
	AND (uri IS NULL or uri is 0)
	AND (piid IS NULL or piid is 0);