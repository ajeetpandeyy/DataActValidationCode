SELECT
    *
FROM award_financial AS af
WHERE af.object_class NOT IN (SELECT object_class_code FROM object_class)
AND af.object_class NOT IN ('0000', '000', '00', '0')
