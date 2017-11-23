SELECT
    *
FROM appropriation
WHERE COALESCE(status_of_budgetary_resour_cpe,0) <> COALESCE(budget_authority_available_cpe,0)

