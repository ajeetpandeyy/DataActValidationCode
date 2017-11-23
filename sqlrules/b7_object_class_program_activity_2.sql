SELECT
    *
FROM object_class_program_activity
WHERE
    COALESCE(gross_outlays_delivered_or_cpe, 0) <>
        (COALESCE(ussgl490200_delivered_orde_cpe, 0) +
        COALESCE(ussgl490800_authority_outl_cpe, 0) +
        COALESCE(ussgl498200_upward_adjustm_cpe, 0))