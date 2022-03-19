if __name__ == "__main__":
    #Run This Code if Being Run From CLI
    import argparse

    #Do Argument Parsing
    parser = argparse.ArgumentParser(description="Perform Admin Commands against the Application", prog="Nastro-Admin")

    parserGroup1 = parser.add_mutually_exclusive_group(required=True)
    parserGroup1.add_argument("-create_new_db",
                              help="Create a fresh database at the current version",
                              action="store_true")
    parserGroup1.add_argument("-upgrade_schema",
                              help="Update an older database to the current version",
                              action="store_true")
    parserGroup1.add_argument("-delete_db",
                              help="Factory Reset the database to the current version",
                              action="store_true")
    parserGroup1.add_argument("-dump_db",
                              help="Dump Database to File",
                              type=argparse.FileType('w', encoding='latin-1'),
                              action="store")
    parserGroup1.add_argument("-import_db",
                              help="Import Database from File",
                              type=open,
                              action="store")
    parserGroup1.add_argument("-db_version", "-db",
                              help="Get the version that the database is running",
                              action="store_true")
    parserGroup1.add_argument("-version", "-v",
                              help="Get the version that the application is running",
                              action="version",
                              version="%(prog)s 0.1")
    
    parser.add_argument("Config Path",
                        help="The path to the config file required by the application (Usually config.json)",
                        type=open,
                        action="store")

    args = parser.parse_args()
    #End Argument Parsing

else:
    #Run This Code if Being Imported
    pass