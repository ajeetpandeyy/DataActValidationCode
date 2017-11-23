from processSQLRules import SQLTable, DataActFile, Validation, Database, processValidationQueries

db = Database("dataActDB.db")

appropriation = DataActFile(db, "appropriation", 2017, 9)
object_class_program_activity = DataActFile(db, "object_class_program_activity", 2017, 9)
award_financial = DataActFile(db, "award_financial", 2017, 9)


if __name__ == "__main__":
    processValidationQueries([award_financial], db)
