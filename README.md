Description: Use SQL rules created by Department of Treasury to create a csv file indicating which appropriation, object class program activity, and award financial records failed or passed validation.

Python Files:
addTables.py --> has sql code for creating tables needed to process validation. Also includes code to upload csv files to database tables. 
                 csv files for databases are in "FilesForDatabase" folder.
createValidationscsv.py --> Run this file to process validations and obtain a csv of all records in appropration, object class progam activity,
                            and award_financial tables and whether the records passed or failed specific validation rules.
processSQLRules --> The bulk of the code. Has classes for DataActFile, Database, SQLTable, and Validation.
                    The Validation class is called when you run createValidationscsv.py. 
                    Class Descriptions:
                         -DataActFile-includes attributes for Database class, table name, name of unique id column
                         -SQLTable-represents each record in "rule_sql" table. Attributes for query name, rule description, rule_sql_id, 
                         whether the rule is a data quality or financial rule, whether the rule involves cross file validation, and whether
                         the rule is fatal or a warning.
                         -Database-attributes for database connection and cursor. Includes methods for adding tables to the database,
                                   and adding records to database via csv file.
                         -Validation-has methods for taking the SQLTable class passed to it, processing the sql rule, and creating a list of
                                     all unique ids of appropriation, object class program activity, or award financial records that failed validation.
                                     includes methods for creating a data dictionary with keys for agency id, fiscal year, period, results (pass or fail),
                                     rule severity, rule description, type of issue (financial or data quality), and a method for writing the data dictionary
                                     to a csv file.
 TestProcessSQLRules --> unit tests for the processSQLRules file                                    
                                     
