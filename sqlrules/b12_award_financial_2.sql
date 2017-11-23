SELECT
    *
FROM award_financial AS af
WHERE COALESCE(LOWER(af.by_direct_reimbursable_fun),'') NOT IN ('', 'r', 'd')
