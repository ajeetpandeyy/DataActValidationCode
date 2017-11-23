from processSQLRules import Database
import os


sql_rules_table = """CREATE TABLE IF NOT EXISTS rule_sql (
                        rule_sql_id integer PRIMARY KEY AUTOINCREMENT,
                        rule_label TEXT,
                        rule_description TEXT,
                        rule_error_message TEXT,
                        rule_cross_file_flag TEXT,
                        file_type TEXT,
                        severity_name TEXT,
                        target_file TEXT,
                        query_name TEXT
                        );"""

appropriation = """CREATE TABLE IF NOT EXISTS appropriation (
                                         id integer PRIMARY KEY AUTOINCREMENT,
                                         adjustments_to_unobligated_cpe numeric,
                                         agency_identifier varchar(3),
                                         allocation_transfer_agency VARCHAR(3),
                                         availability_type_code VARCHAR(1),
                                        beginning_period_of_availa VARCHAR(4),
                                        borrowing_authority_amount_cpe NUMERIC,
                                        budget_authority_appropria_cpe NUMERIC,
                                        budget_authority_available_cpe NUMERIC,
                                        budget_authority_unobligat_fyb NUMERIC,
                                        contract_authority_amount_cpe NUMERIC,
                                        deobligations_recoveries_r_cpe NUMERIC,
                                        ending_period_of_availabil VARCHAR(4),
                                        gross_outlay_amount_by_tas_cpe NUMERIC,
                                        main_account_code VARCHAR(4),
                                        obligations_incurred_total_cpe NUMERIC,
                                        other_budgetary_resources_cpe NUMERIC,
                                        spending_authority_from_of_cpe NUMERIC,
                                        status_of_budgetary_resour_cpe NUMERIC,
                                        sub_account_code VARCHAR(3),
                                        unobligated_balance_cpe NUMERIC,
                                        fiscal_year VARCHAR(4),
                                        period VARCHAR(2),
                                        tas VARCHAR(20),
                                        tas_with_sub text
                                         );"""

sf_133 = """CREATE TABLE IF NOT EXISTS sf_133 (
            sf133_id integer PRIMARY KEY AUTOINCREMENT,
            agency_identifier TEXT,
            allocation_transfer_agency TEXT,
            availability_type_code TEXT,
            beginning_period_of_availa TEXT,
            ending_period_of_availabil TEXT,
            main_account_code TEXT,
            sub_account_code TEXT,
            tas TEXT,
            fiscal_year INTEGER,
            period INTEGER,
            line INTEGER,
            amount NUMERIC
            );"""


object_class_program_activity = '''CREATE TABLE IF NOT EXISTS object_class_program_activity
(
  
  id integer PRIMARY KEY AUTOINCREMENT,
  agency_identifier text,
  allocation_transfer_agency text,
  availability_type_code text,
  beginning_period_of_availa text,
  by_direct_reimbursable_fun text,
  deobligations_recov_by_pro_cpe numeric,
  ending_period_of_availabil text,
  gross_outlay_amount_by_pro_cpe numeric,
  gross_outlay_amount_by_pro_fyb numeric,
  gross_outlays_delivered_or_cpe numeric,
  gross_outlays_delivered_or_fyb numeric,
  gross_outlays_undelivered_cpe numeric,
  gross_outlays_undelivered_fyb numeric,
  main_account_code text,
  object_class text,
  obligations_delivered_orde_cpe numeric,
  obligations_delivered_orde_fyb numeric,
  obligations_incurred_by_pr_cpe numeric,
  obligations_undelivered_or_cpe numeric,
  obligations_undelivered_or_fyb numeric,
  program_activity_code text,
  program_activity_name text,
  sub_account_code text,
  ussgl480100_undelivered_or_cpe numeric,
  ussgl480100_undelivered_or_fyb numeric,
  ussgl480200_undelivered_or_cpe numeric,
  ussgl480200_undelivered_or_fyb numeric,
  ussgl483100_undelivered_or_cpe numeric,
  ussgl483200_undelivered_or_cpe numeric,
  ussgl487100_downward_adjus_cpe numeric,
  ussgl487200_downward_adjus_cpe numeric,
  ussgl488100_upward_adjustm_cpe numeric,
  ussgl488200_upward_adjustm_cpe numeric,
  ussgl490100_delivered_orde_cpe numeric,
  ussgl490100_delivered_orde_fyb numeric,
  ussgl490200_delivered_orde_cpe numeric,
  ussgl490800_authority_outl_cpe numeric,
  ussgl490800_authority_outl_fyb numeric,
  ussgl493100_delivered_orde_cpe numeric,
  ussgl497100_downward_adjus_cpe numeric,
  ussgl497200_downward_adjus_cpe numeric,
  ussgl498100_upward_adjustm_cpe numeric,
  ussgl498200_upward_adjustm_cpe numeric,
  fiscal_year TEXT,
  period TEXT,
  tas text NOT NULL,
  tas_with_sub TEXT
);'''

object_class = '''CREATE TABLE if not exists object_class
(
  
  object_class_id serial NOT NULL,
  object_class_code text NOT NULL,
  object_class_name text
  
);'''

award_financial = '''CREATE TABLE if not exists award_financial
(
  id integer PRIMARY KEY AUTOINCREMENT,
  agency_identifier text,
  allocation_transfer_agency text,
  availability_type_code text,
  beginning_period_of_availa text,
  by_direct_reimbursable_fun text,
  deobligations_recov_by_awa_cpe numeric,
  ending_period_of_availabil text,
  fain text,
  gross_outlay_amount_by_awa_cpe numeric,
  gross_outlay_amount_by_awa_fyb numeric,
  gross_outlays_delivered_or_cpe numeric,
  gross_outlays_delivered_or_fyb numeric,
  gross_outlays_undelivered_cpe numeric,
  gross_outlays_undelivered_fyb numeric,
  main_account_code text,
  object_class text,
  obligations_delivered_orde_cpe numeric,
  obligations_delivered_orde_fyb numeric,
  obligations_incurred_byawa_cpe numeric,
  obligations_undelivered_or_cpe numeric,
  obligations_undelivered_or_fyb numeric,
  parent_award_id text,
  piid text,
  program_activity_code text,
  program_activity_name text,
  sub_account_code text,
  transaction_obligated_amou numeric,
  uri text,
  ussgl480100_undelivered_or_cpe numeric,
  ussgl480100_undelivered_or_fyb numeric,
  ussgl480200_undelivered_or_cpe numeric,
  ussgl480200_undelivered_or_fyb numeric,
  ussgl483100_undelivered_or_cpe numeric,
  ussgl483200_undelivered_or_cpe numeric,
  ussgl487100_downward_adjus_cpe numeric,
  ussgl487200_downward_adjus_cpe numeric,
  ussgl488100_upward_adjustm_cpe numeric,
  ussgl488200_upward_adjustm_cpe numeric,
  ussgl490100_delivered_orde_cpe numeric,
  ussgl490100_delivered_orde_fyb numeric,
  ussgl490200_delivered_orde_cpe numeric,
  ussgl490800_authority_outl_cpe numeric,
  ussgl490800_authority_outl_fyb numeric,
  ussgl493100_delivered_orde_cpe numeric,
  ussgl497100_downward_adjus_cpe numeric,
  ussgl497200_downward_adjus_cpe numeric,
  ussgl498100_upward_adjustm_cpe numeric,
  ussgl498200_upward_adjustm_cpe numeric,
  fiscal_year text,
  period text,
  tas text NOT NULL,
  tas_with_sub text
  
);'''

if __name__ == "__main__":
    database = Database("dataActDB.db")
    if database.conn is not None:
        database.create_table(sql_rules_table)
        database.create_table(appropriation)
        database.create_table(sf_133)
        database.create_table(object_class_program_activity)
        database.create_table(object_class)
        database.create_table(award_financial)
    else:
        print("Error! cannot create database connection.")
    database.add_csv_to_database("rule_sql", os.getcwd() + "\\FilesForDatabase\\sqlRulesSoFar.csv")
    database.add_csv_to_database("sf_133", os.getcwd() + "\\FilesForDatabase\\sf133_2017_09.csv")
    database.add_csv_to_database("appropriation", os.getcwd() + "\\FilesForDatabase\\appropriation.csv")
    database.add_csv_to_database("object_class_program_activity", os.getcwd() + "\\FilesForDatabase\\object_class_program_activity.csv")
    database.add_csv_to_database("object_class", os.getcwd() + "\\FilesForDatabase\\object_class.csv")
    database.add_csv_to_database("award_financial", os.getcwd() + "\\FilesForDatabase\\award_financial.csv")

