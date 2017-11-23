import sqlite3
import unittest
import os
import pandas as pd
from processSQLRules import Database, DataActFile, SQLTable, Validation, ExecuteQuery
from processSQLRules import processValidationQueries, map_file_names_to_sql_table

testDB = os.getcwd() + "\\testFolder\\TestDB.db"
db = Database(testDB)

'''
Tested everything from processSQLRulesv4 except the following:
    * processValidationQueries function: 
        doesn't return anything, other than looping through each sql rule for 
        a specific file type, this function is essentially just initializing 
        the Validation class and writing the pass and fail data dictionaries to 
        a csv file.
    * Validation().write_results_to_csv(self, all_headings) method:
        just converting dictionary to pandas data frame and writing results
        to csv. All code is basically from pandas.
'''



class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.testDB = os.getcwd() + "\\testFolder\\TestDB.db"

    def createMockTable(self):
        sql = '''CREATE table if not exists appropriation
        (id integer PRIMARY KEY AUTOINCREMENT,
        first_field TEXT,
        second_field TEXT
        );'''
        return sql

    def testInitializeDatabase(self):
        db = Database(self.testDB)
        self.assertIsNotNone(db.create_connection())
        self.assertIsNotNone(db.conn)
        self.assertIsNotNone(db.cur)
        db.close_connection()

    def testCreateTable(self):
        db = Database(self.testDB)
        sql = self.createMockTable()
        db.create_table(sql)
        get_table_sql = '''SELECT name FROM sqlite_master where type='table' AND
                           name="appropriation"'''
        db.cur.execute(get_table_sql)
        get_table = db.cur.fetchone()[0]
        self.assertEqual(get_table, "appropriation")
        db.close_connection()

    def testAddingCSVToDatabase(self):
        db = Database(self.testDB)
        getCSV = os.getcwd() + "\\testFolder\\testDatabaseCSV.csv"
        db.add_csv_to_database("appropriation", getCSV)
        test_sql = '''SELECT * from appropriation'''
        db.cur.execute(test_sql)
        results = db.cur.fetchall()
        first_result = results[0]
        second_result = results[1]
        self.assertEqual(first_result, (0, "barbara", "red"))
        self.assertEqual(second_result, (1, "sarah", "yellow"))
        db.cur.execute('''Delete from appropriation''')
        db.close_connection()

    def testAddCSVToExistingData(self):
        #TODO: this test is repetitve with one above, combine or make them have their own setup and teardown
        # in df.to_sql code we have if_exists='append',
        # This test is to make sure it's appending properly.
        db = Database(self.testDB)
        db.cur.execute('Delete from appropriation')
        db.conn.commit()
        getCSV = os.getcwd() + "\\testFolder\\testDatabaseCSV.csv"
        db.add_csv_to_database("appropriation", getCSV)
        db.add_csv_to_database("appropriation", getCSV)
        # csv has 2 records, so should be 4 now
        test_sql = '''SELECT first_field, second_field from appropriation'''
        db.cur.execute(test_sql)
        results = db.cur.fetchall()
        self.assertEqual(len(results), 4)


class TestSQLTableClass(unittest.TestCase):

    def setUp(self):
        self.db = Database(os.getcwd() + "\\testFolder\\testDB.db")
        self.testSQLInstance = SQLTable(self.db, 1)

    def test_initialize_database(self):
        # test database connection created when initialized
        self.assertIsNotNone(self.db.conn)

    def test_initialization_unique_id_table_name(self):
        self.assertEqual(self.testSQLInstance.unique_id_value, 1)
        self.assertEqual(self.testSQLInstance.unique_id_name, "rule_sql_id")
        self.assertEqual(self.testSQLInstance.table_name, "rule_sql")

    def test_initialization_data_quality_rules(self):
        data_quality_rules = ['b11_award_financial_1', 'b11_object_class_program_activity_1',
                              'a30_appropriations', 'a32_appropriations', 'a33_appropriations_1',
                              'a33_appropriations_2', 'b20_object_class_program_activity',
                              'fabs2_detached_award_financial_assistance_2']
        self.assertEqual(data_quality_rules, self.testSQLInstance.data_quality_rules)

    # refer to testSQLRules.csv for order that records added to sql table.
    # based on the fact that our set up passed unique id 1, we should be pulling
    # information from the second record.
    def test_test_name(self):
        # refer to file testDatabaseSetUp for creation of sql table

        self.assertEqual("a1_object_class_program_activity", self.testSQLInstance.test_name)

    def test_rule_description(self):
        # TODO: figure out how to get this test to work without having the whole thing on one line.
        # if you make it multi-line and spacing isn't perfect, test will fail.
        rule_description = '''TAS components: The combination of all the elements that make up the TAS must match the Treasury Central Accounting Reporting System (CARS). AgencyIdentifier, MainAccountCode, and SubAccountCode are always required. AllocationTransferAgencyIdentifier, BeginningPeriodOfAvailability, EndingPeriodOfAvailability and AvailabilityTypeCode are required if present in the CARS table.'''
        self.assertEqual(rule_description, self.testSQLInstance.rule_description)

    def test_rule_cross_file_flag(self):
        self.assertEqual('n', self.testSQLInstance.rule_cross_file_flag)

    def test_type_of_issue(self):
        self.assertEqual('financial', self.testSQLInstance.type_of_issue)

    def test_severity(self):
        self.assertEqual('fatal', self.testSQLInstance.severity)

    def tearDown(self):
        self.db.close_connection()

class TestDataFileClass(unittest.TestCase):

    def setUp(self):
        self.db = Database(os.getcwd() + "\\testFolder\\testDB.db")
        self.testDataFileInstance = DataActFile(self.db, "object_class_program_activity", 2017, 9)

    def tearDown(self):
        self.db.close_connection()


    def test_database(self):
        self.assertEqual(self.db, self.testDataFileInstance.database)

    def test_table_name(self):
        self.assertEqual("object_class_program_activity", self.testDataFileInstance.table_name)

    def test_fiscal_year(self):
        self.assertEqual(2017, self.testDataFileInstance.fiscal_year)

    def test_period(self):
        self.assertEqual(9, self.testDataFileInstance.period)

    def test_file_type_sql_table(self):
        self.assertEqual("program_activity", self.testDataFileInstance.file_type_sql_table)

    def test_unique_id_name(self):
        self.assertEqual("id", self.testDataFileInstance.unique_id_name)

    # need to get a list (tuple?) of records in order to run the unique headings test
    def get_records_for_unique_headings_test(self):
        sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        print(sql_path)
        sql_path =os.getcwd() + "\\sqlrules\\b3_object_class_program_activity_2.sql"
        with open(sql_path, 'r') as fd:
            sqlFile = fd.read()
        self.db.cur.execute(sqlFile)
        failing_records = self.db.cur.fetchall()
        return failing_records

    def test_get_records_for_unqiue_headings(self):
        failing_records = self.get_records_for_unique_headings_test()
        attribute_list = self.testDataFileInstance.get_records_for_unique_headings(failing_records, "tas")
        # i ran the query manually. There are 55 rows returned.
        """TODO: tas are supposed to have ATA as first 3 digits. consider updating
        test csv so that tas match proper pattern. then redo test assertions
        to account for this"""
        self.assertEqual(len(attribute_list), 55)
        self.assertEqual(attribute_list[0], "069-0000-0000-X-1301")
        self.assertEqual(attribute_list[1], "069-0000-0000-X-4562")
        self.assertEqual(attribute_list[2], "069-0000-0000-X-4562")
        self.assertEqual(attribute_list[6], "069-0000-0000-X-8106")
        self.assertEqual(attribute_list[7], "069-0000-0000-X-8107")

class TestValidationClass(unittest.TestCase):

    def setUp(self):
        self.db = Database(os.getcwd() + "\\testFolder\\testDB.db")
        self.mockDataFile = DataActFile(self.db, "object_class_program_activity", 2017, 9)
        self.mockSQL = SQLTable(self.db, 32)  # this is b3_object_class_progam_activity_2
        self.testValidation = Validation(self.db, self.mockDataFile, self.mockSQL)

    def tearDown(self):
        self.db.close_connection()

    def test_database(self):
        self.assertEqual(self.db, self.testValidation.database)

    def test_data_act_file_attribute(self):
        self.assertEqual(self.mockDataFile, self.testValidation.data_act_file)

    def test_sql_rule_attribute(self):
        self.assertEqual(self.mockSQL, self.testValidation.sqlRule)

    def test_failing_records_attribute(self):
        self.assertEqual(55, len(self.testValidation.failing_records))

    def test_fail_tuple_ids_attribute(self):
        self.assertIn(4, self.testValidation.fail_tuple_of_ids)
        self.assertIn(92, self.testValidation.fail_tuple_of_ids)
        self.assertIn(120, self.testValidation.fail_tuple_of_ids)
        self.assertIn(136, self.testValidation.fail_tuple_of_ids)
        self.assertIn(142, self.testValidation.fail_tuple_of_ids)
        self.assertIn(154, self.testValidation.fail_tuple_of_ids)
        self.assertIn(188, self.testValidation.fail_tuple_of_ids)
        self.assertIn(250, self.testValidation.fail_tuple_of_ids)
        self.assertIn(564, self.testValidation.fail_tuple_of_ids)
        self.assertIn(606, self.testValidation.fail_tuple_of_ids)

    def test_pass_list_of_ids_attribute(self):
        # 4288 is total number of records, 55 failed validation
        count = 4288 - 55
        self.assertEqual(count, len(self.testValidation.pass_list_of_ids))
        self.assertIn(0, self.testValidation.pass_list_of_ids)
        self.assertIn(93, self.testValidation.pass_list_of_ids)
        self.assertIn(94, self.testValidation.pass_list_of_ids)
        self.assertIn(119, self.testValidation.pass_list_of_ids)
        self.assertNotIn(92, self.testValidation.pass_list_of_ids)

    def test_number_of_records_pass_attribute(self):
        count = 4288 - 55
        self.assertEqual(count, self.testValidation.number_of_records_pass)

    def test_number_of_records_fail_attribtue(self):
        self.assertEqual(55, self.testValidation.number_of_records_fail)

    def test_fail_dictionary_attribute(self):
        # test a few of the fail ids to make sure they're in dictionary
        # test some pass ids to make sure not in dictionary
        for i in [4, 92, 120, 136]:
            self.assertIn(i, self.testValidation.fail_data_dictionary.get('Original Table Id'))
        for i in [0, 1, 2, 3, 91, 93, 119, 121]:
            self.assertNotIn(i, self.testValidation.fail_data_dictionary.get('Original Table Id'))
        file_type = self.testValidation.fail_data_dictionary.get('File Type')
        self.assertEqual(['object_class_program_activity'] * 55, file_type)
        agency_id_list = self.testValidation.fail_data_dictionary.get('Agency Id')
        # all agency ids that failed validation were 69
        self.assertEqual(['69'] * 55, agency_id_list)
        # see the data act file test for get_unique_headings-I did a few more tas tests there
        self.assertIn('069-0000-0000-X-1301', self.testValidation.fail_data_dictionary.get('tas'))
        self.assertEqual([2017] * 55, self.testValidation.fail_data_dictionary.get('Fiscal Year'))
        self.assertEqual([9] * 55, self.testValidation.fail_data_dictionary.get('Period'))
        self.assertEqual(['b3_object_class_program_activity_2'] * 55, self.testValidation.fail_data_dictionary.get('Test Name'))
        self.assertEqual(['fail'] * 55, self.testValidation.fail_data_dictionary.get('Results'))
        self.assertEqual(['warning'] * 55, self.testValidation.fail_data_dictionary.get('Severity'))
        self.assertEqual(['financial'] * 55, self.testValidation.fail_data_dictionary.get('Type of Issue'))
        # skip rule description. its too long. if the rest of these work, rule description works.
        self.assertEqual(['n'] * 55, self.testValidation.fail_data_dictionary.get('Rule Cross File Flag'))

    def test_pass_dictionary_attribute(self):
        # only going to test the dictionary values that are different from the fail dictionary
        count = 4288 - 55
        for i in [0, 1, 2, 3, 91, 93, 119, 121]:
            self.assertIn(i, self.testValidation.pass_data_dictionary.get('Original Table Id'))
        for i in [4, 92, 120, 136]:
            self.assertNotIn(i, self.testValidation.pass_data_dictionary.get('Original Table Id'))
        for i in ["12", "14", "17", "21", "309", "57", "97"]:
            self.assertIn(i, self.testValidation.pass_data_dictionary.get('Agency Id'))
        for i in ['069-0000-0000-X-1301', '069-0000-0000-X-4120', '069-0000-0000- -8107']:
            self.assertIn(i, self.testValidation.pass_data_dictionary.get('tas'))
        self.assertEqual(count, len(self.testValidation.pass_data_dictionary.get('tas')))
        self.assertEqual(['pass'] * count, self.testValidation.pass_data_dictionary.get('Results') )

class TestExecuteQueryClass(unittest.TestCase):

    def setUp(self):
        self.db = db
        self.mockSQL = SQLTable(self.db, 0)

    def test_query_single_value(self):
        get_query_name = self.mockSQL.query_single_value(0, "query_name")
        self.assertEqual("a1_appropriations", get_query_name)

if __name__ == '__main__':
    unittest.main()





