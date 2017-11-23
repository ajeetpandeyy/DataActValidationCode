SELECT *
FROM award_financial
WHERE (piid IS NOT NULL and piid is not 0)
	AND ((fain IS NOT NULL and fain is not 0) OR (uri IS NOT NULL and uri is not 0))