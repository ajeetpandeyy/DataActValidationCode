import  sqlite3
import os
import pandas as pd

testDB = os.getcwd() + "\\TestDB.db"

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
  tas TEXT NOT NULL,
  tas_with_sub TEXT
);'''

# separate function because we do this once for all of testing
def create_and_populate_sql_table():
    conn = sqlite3.connect(testDB)
    sql = """CREATE TABLE if not exists rule_sql (
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

    conn.cursor().execute(sql)
    conn.commit()

def add_data_to_rule_sql():
    conn = sqlite3.connect(testDB)
    getCSV = os.getcwd() + "\\testSqlRules.csv"
    df = pd.read_csv(getCSV)
    df.to_sql("rule_sql", conn, if_exists='append', index=True, index_label="rule_sql_id")
    conn.close()

def create_program_activity_table_and_populate():
    conn = sqlite3.connect(testDB)
    conn.cursor().execute(object_class_program_activity)
    getCSV = os.getcwd() + "\\testObjectClassProgramActivity.csv"
    df = pd.read_csv(getCSV)
    df.to_sql("object_class_program_activity", conn, if_exists='append', index=True, index_label="id")
    conn.close()



if __name__ == "__main__":
    #create_and_populate_sql_table()
    #add_data_to_rule_sql()
    create_program_activity_table_and_populate()