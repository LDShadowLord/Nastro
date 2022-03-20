if __name__ == "__main__":
    #Run This Code if Being Run From CLI
    import argparse

    #Do Argument Parsing
    parser = argparse.ArgumentParser(description="Perform Tape Commands against the Application", prog="Nastro-Tape")
    
    exclusiveGroup = parser.add_mutually_exclusive_group()
    exclusiveGroup.add_argument("-delete_tape", "-delete",
                              help="Delete a Tape from the DB",
                              action="store_true")
    exclusiveGroup.add_argument("-move_tape", "-move",
                              help="Move a Tape between Locations",
                              action="store_true")
    exclusiveGroup.add_argument("-load_tape", "-load",
                              help="Load a Tape into a Library",
                              action="store_true")
    exclusiveGroup.add_argument("-unload_tape", "-unload",
                              help="Unload a Tape from a Library",
                              action="store_true")
    exclusiveGroup.add_argument("-new_tape", "-new",
                              help="Add a new Tape to the DB",
                              action="store_true")
    exclusiveGroup.add_argument("-edit_tape", "-edit",
                              help="Edit a Tape in the DB",
                              action="store_true")

    parser.add_argument("-location", "-lo",
                        help="The 6 character location ID",
                        action="store")
    parser.add_argument("-type", "-ty",
                        help="The tape type (ex: LTO6/SDLT 4)",
                        action="store")
    parser.add_argument("-software", "-sw",
                        help="The backup software type (ex: LTFS/Netbackup 7.1.7)",
                        action="store")
    parser.add_argument("-library", "-li",
                        help="The library that the tape is being placed in",
                        action="store")
    parser.add_argument("-slot", "-sl",
                        help="The slot that the tape is being moved to",
                        type=int,
                        action="store")

    parser.add_argument("--destroy",
                        help="Add if you want the tape to be marked as destroyed.",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--scratch",
                        help="Add if you want the tape to be marked as scratch.",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--config",
                        help="The path to the config file required by the application",
                        default="config.json",
                        type=open,
                        action="store")
    
    parser.add_argument("Tape Barcode",
                        help="The 8 character barcode used to identify the tape",
                        action="store")    

    args = parser.parse_args()
    #End Argument Parsing

else:
    #Run This Code if Being Imported
    pass
