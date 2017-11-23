import pandas as pd
import os
import sqlite3



map_file_names_to_sql_table = {
    'appropriation': ['appropriations', "id"],
    'object_class_program_activity': ['program_activity', "id"],
    'award_financial': ['award_financial', "id"],
}

def processValidationQueries(table_names, database):
    for table in table_names:
        exec_rules = database.cur.execute("SELECT * FROM rule_sql where file_type = ?", (table.file_type_sql_table,))
        sql_rules = database.cur.fetchall()
        for rule in sql_rules:
            sqlRule = SQLTable(database, rule[0])
            validation = Validation(database, table, sqlRule)
            validation.write_results_to_csv(validation.fail_data_dictionary)
            validation.write_results_to_csv(validation.pass_data_dictionary)

class ExecuteQuery(object):

    def query_single_value(self, unique_id_value, column_name):
        unique_id_value = str(unique_id_value)

        sql = "SELECT {cn} from {tn} where {idn}=(?)".format(cn=column_name, tn=self.table_name,
                                                       idn=self.unique_id_name)
        self.database.cur.execute(sql, (unique_id_value,))
        result = self.database.cur.fetchone()
        try:
            result = result[0]
        except:
            raise ValueError("single query failed for %s in %s returning %s" % (unique_id_value, self.table_name, column_name))
        return result


class SQLTable(ExecuteQuery):

    def __init__(self, database, unique_id_value):
        self.database = database
        self.database.create_connection()
        self.data_quality_rules = self.get_data_quality_rules()
        self.unique_id_name = "rule_sql_id"
        self.table_name = "rule_sql"
        self.unique_id_value = unique_id_value
        self.test_name = self.query_single_value(self.unique_id_value, "query_name")
        self.rule_description = self.query_single_value(self.unique_id_value, "rule_description")
        self.rule_cross_file_flag = self.query_single_value(self.unique_id_value, "rule_cross_file_flag")
        self.type_of_issue = self.get_type_of_issue()
        self.severity = self.query_single_value(self.unique_id_value, "severity_name")

    def get_data_quality_rules(self):
        return ['b11_award_financial_1', 'b11_object_class_program_activity_1',
                              'a30_appropriations', 'a32_appropriations', 'a33_appropriations_1',
                              'a33_appropriations_2', 'b20_object_class_program_activity',
                              'fabs2_detached_award_financial_assistance_2']

    def get_type_of_issue(self):
        if self.test_name in self.data_quality_rules:
            self.type_of_issue = "data quality"
        else:
            self.type_of_issue = "financial"
        return self.type_of_issue


class DataActFile(ExecuteQuery):

    def __init__(self, database, table_name, fiscal_year, period):
        self.database = database
        self.table_name = table_name
        self.fiscal_year = fiscal_year
        self.period = period
        self.file_type_sql_table = map_file_names_to_sql_table.get(self.table_name)[0]
        self.unique_id_name = map_file_names_to_sql_table.get(self.table_name)[1]


    def get_records_for_unique_headings(self, records, column_name):
        attribute_list = []
        for row in records:
            new_value = self.query_single_value(row[0], column_name)
            attribute_list.append(new_value)
        return attribute_list

class Validation(object):



    def __init__(self, database, dataActFile, sqlRule):
        self.database = database
        self.data_act_file = dataActFile
        self.sqlRule = sqlRule
        self.failing_records = self.get_failing_records()
        self.fail_tuple_of_ids = self.get_tuple_fail_ids()
        self.passing_records = self.get_passing_records()
        self.fail_list_of_ids = list(self.fail_tuple_of_ids)
        self.pass_list_of_ids = self.get_list_pass_ids()
        self.number_of_records_pass = len(self.passing_records)
        self.number_of_records_fail = len(self.failing_records)
        self.fail_data_dictionary = self.get_data_dictionary(self.fail_list_of_ids, self.failing_records, self.number_of_records_fail, "fail")
        self.pass_data_dictionary = self.get_data_dictionary(self.pass_list_of_ids, self.passing_records, self.number_of_records_pass, "pass")
        self.database.close_connection()


    def get_data_dictionary(self, list_of_ids, records, number_of_records, results):
        all_headings = {
            'Original Table Id': list_of_ids,
            'File Type': [self.data_act_file.table_name] * number_of_records,
            'Agency Id': self.data_act_file.get_records_for_unique_headings(records, "agency_identifier"),
            'tas': self.data_act_file.get_records_for_unique_headings(records, "tas"),
            'Fiscal Year': [self.data_act_file.fiscal_year] * number_of_records,
            'Period': [self.data_act_file.period] * number_of_records,
            'Test Name': [self.sqlRule.test_name] * number_of_records,
            'Results': [results] * number_of_records,
            'Severity': [self.sqlRule.severity] * number_of_records,
            'Type of Issue': [self.sqlRule.type_of_issue] * number_of_records,
            'Rule Description': [self.sqlRule.rule_description] * number_of_records,
            'Rule Cross File Flag': [self.sqlRule.rule_cross_file_flag] * number_of_records
        }
        return all_headings


    def get_failing_records(self):
        current_path = os.getcwd()
        abs_path = current_path + "\\sqlrules\\"
        full_path = abs_path + self.sqlRule.test_name + ".sql"
        with open(full_path, 'r') as fd:
            sqlFile = fd.read()
        self.database.cur.execute(sqlFile)
        failing_records = self.database.cur.fetchall()
        return failing_records

    def get_tuple_fail_ids(self):
        all_ids = ()
        for row in self.failing_records:
            all_ids = all_ids + (row[0],)
        return all_ids

    def get_passing_records(self):
        string_all_ids = str(self.fail_tuple_of_ids)
        if len(self.fail_tuple_of_ids) == 1:
            string_all_ids = string_all_ids.replace(",", "")
        # select everything that did not match the original query.
        # These are all the rows that passed validation.
        sql = '''
                      SELECT * from %s
                      WHERE %s not in %s''' % (self.data_act_file.table_name, self.data_act_file.unique_id_name, string_all_ids)
        self.database.cur.execute(sql)
        self.passing_records = self.database.cur.fetchall()
        return self.passing_records

    def get_list_pass_ids(self):
        passing_ids = ()
        for row in self.passing_records:
            passing_ids = passing_ids + (row[0],)
        return list(passing_ids)

    def write_results_to_csv(self, all_headings):
        all_headings = pd.DataFrame(all_headings)
        with open('validation2.csv', 'a') as f:
            all_headings.to_csv(f, header=True)





class Database(object):

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = self.create_connection()
        self.cur = self.conn.cursor()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return self.conn
        except sqlite3.Error as e:
            print(e)
            return None

    def add_csv_to_database(self, table_name, csv_file):
        df = pd.read_csv(csv_file)
        self.conn = self.create_connection()
        get_label = map_file_names_to_sql_table.get(table_name)[1]
        df.to_sql(table_name, self.conn, if_exists='append', index=True, index_label=get_label)

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def close_connection(self):
        self.conn.close()

