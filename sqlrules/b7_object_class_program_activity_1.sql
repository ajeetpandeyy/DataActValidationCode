SELECT
    *
FROM object_class_program_activity
WHERE
    COALESCE(gross_outlays_delivered_or_fyb, 0) <> COALESCE(ussgl490800_authority_outl_fyb, 0)