SELECT
    *
FROM appropriation
WHERE COALESCE(other_budgetary_resources_cpe,0) <> COALESCE(contract_authority_amount_cpe,0) + COALESCE(borrowing_authority_amount_cpe,0) + COALESCE(spending_authority_from_of_cpe,0)

