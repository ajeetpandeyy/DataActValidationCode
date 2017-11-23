-- Verify that all of the submitted data (from file A) has an associated GTAS
select * from appropriation as approp where
approp.tas not in (select tas from sf_133 as sf where approp.fiscal_year = sf.fiscal_year
and approp.period = sf.period)

    AND (
        COALESCE(approp.adjustments_to_unobligated_cpe,0) <> 0
        OR COALESCE(approp.budget_authority_appropria_cpe,0) <> 0
        OR COALESCE(approp.borrowing_authority_amount_cpe,0) <> 0
        OR COALESCE(approp.contract_authority_amount_cpe,0) <> 0
        OR COALESCE(approp.spending_authority_from_of_cpe,0) <> 0
        OR COALESCE(approp.other_budgetary_resources_cpe,0) <> 0
        OR COALESCE(approp.budget_authority_available_cpe,0) <> 0
        OR COALESCE(approp.gross_outlay_amount_by_tas_cpe,0) <> 0
        OR COALESCE(approp.obligations_incurred_total_cpe,0) <> 0
        OR COALESCE(approp.deobligations_recoveries_r_cpe,0) <> 0
        OR COALESCE(approp.unobligated_balance_cpe,0) <> 0
        OR COALESCE(approp.status_of_budgetary_resour_cpe,0) <> 0
    );


