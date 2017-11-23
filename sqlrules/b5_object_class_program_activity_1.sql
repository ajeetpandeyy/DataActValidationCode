SELECT
    *
FROM object_class_program_activity
WHERE
    COALESCE(gross_outlay_amount_by_pro_fyb, 0) <>
        (COALESCE(gross_outlays_undelivered_fyb, 0) +
        COALESCE(gross_outlays_delivered_or_fyb, 0))