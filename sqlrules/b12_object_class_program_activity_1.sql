SELECT
    *
FROM object_class_program_activity as op
WHERE (
    COALESCE(op.ussgl480100_undelivered_or_fyb, 0) <> 0
    OR COALESCE(op.ussgl480100_undelivered_or_cpe, 0) <> 0
    OR COALESCE(op.ussgl488100_upward_adjustm_cpe, 0) <> 0
    OR COALESCE(op.ussgl490100_delivered_orde_fyb, 0) <> 0
    OR COALESCE(op.ussgl490100_delivered_orde_cpe, 0) <> 0
    OR COALESCE(op.ussgl498100_upward_adjustm_cpe, 0) <> 0
    OR COALESCE(op.ussgl480200_undelivered_or_cpe, 0) <> 0
    OR COALESCE(op.ussgl480200_undelivered_or_fyb, 0) <> 0
    OR COALESCE(op.ussgl488200_upward_adjustm_cpe, 0) <> 0
    OR COALESCE(op.ussgl490200_delivered_orde_cpe, 0) <> 0
    OR COALESCE(op.ussgl490800_authority_outl_fyb, 0) <> 0
    OR COALESCE(op.ussgl490800_authority_outl_cpe, 0) <> 0
    OR COALESCE(op.ussgl498200_upward_adjustm_cpe, 0) <> 0) AND
    LENGTH(COALESCE(op.object_class, '')) = 3 AND
    COALESCE(op.by_direct_reimbursable_fun, '') = ''