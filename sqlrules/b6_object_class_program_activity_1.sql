SELECT
    *
FROM object_class_program_activity
WHERE
    COALESCE(gross_outlays_undelivered_fyb, 0) <> COALESCE(ussgl480200_undelivered_or_fyb, 0)