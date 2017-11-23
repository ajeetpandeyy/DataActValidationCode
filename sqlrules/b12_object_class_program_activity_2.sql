SELECT
    *
FROM object_class_program_activity AS op
WHERE COALESCE(LOWER(op.by_direct_reimbursable_fun),'') NOT IN ('', 'r', 'd')
