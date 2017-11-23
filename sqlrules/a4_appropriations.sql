SELECT
    *
FROM appropriation
WHERE COALESCE(status_of_budgetary_resour_cpe,0) <> COALESCE(obligations_incurred_total_cpe,0) + COALESCE(unobligated_balance_cpe,0)

