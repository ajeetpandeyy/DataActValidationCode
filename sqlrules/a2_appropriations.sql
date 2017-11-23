SELECT
    *
FROM appropriation
WHERE COALESCE(budget_authority_available_cpe,0) <> COALESCE(budget_authority_appropria_cpe,0) + COALESCE(budget_authority_unobligat_fyb,0) + COALESCE(adjustments_to_unobligated_cpe,0) + COALESCE(other_budgetary_resources_cpe,0)

