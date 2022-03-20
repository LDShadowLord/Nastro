# Internal Imports
from sqlalchemy.exc import IntegrityError
import db
from __version__ import *
global nastroVersion, nastroVersionZ

def createNewDB(config):
    try:
        import sqlalchemy.orm
        import sqlalchemy
        import socket

        db.Base.metadata.create_all(db.primary_engine)

        with sqlalchemy.orm.Session(db.primary_engine) as session:
            default_admin = db.Admin(
                admin_id=True,
                admin_version=nastroVersion,
                admin_hostname=str(socket.gethostname()),
                admin_user_cred="root"
                )

            default_location = db.Location(
                location_id="NASTRO",
                location_display_name="Nastro Default Pool",
                location_address="123 ABC Street",
                location_vault="NoVault",
                location_slots="123456"
                )
            default_library = db.Library(
                library_id = "NASTRO-DEFAULT",
                library_display_name = "Default Library for Nastro",
                library_location = "NASTRO",
                library_model = "GenericModel",
                library_manufacturer = "Tycoonier",
                library_slots = 123456,
                library_ip = "127.0.0.1",
                library_user_cred = "admin",
                library_user_pass = "password"
                )

            default_tape = db.Tape(
                tape_barcode = "NST001",
                tape_location = "NASTRO",
                tape_destroyed = False,
                tape_type = "VTL",
                tape_barcode_trunc = "NST001",
                tape_scratch = False,
                tape_library = "NASTRO-DEFAULT",
                tape_software = "LTFS",
                tape_slot = 1
                )
            default_tape_details = db.Tape_Details(
                tape_barcode = "NST001",
                tape_description = "The default tape added by Nastro on a fresh database. Feel free to delete this tape.",
                tape_condition = "Good",
                tape_serial = None,
                tape_manufacturer = "Tycoonier",
                tape_encryption_key = None,
                tape_hash = None
                )

            default_audit = db.Audit(
                audit_version = nastroVersion,
                audit_hostname = str(socket.gethostname()),
                audit_action = {
                    0: "Created new Database",
                    1: "Admin Values Populated",
                    2: "Location [NASTRO] Added to Database",
                    3: "Library [NASTRO-DEFAULT] Added to Database",
                    4: "Tape [NST001] Added to Database",
                    5: "Tape Details Populated for Tape [NST001]"
                    },
                audit_count = 6
                )
            session.add_all([
                default_admin,
                default_location,
                default_library,
                default_tape,
                default_tape_details,
                default_audit])
            session.commit()
    except sqlalchemy.exc.IntegrityError:
        print("[ERROR] You must wipe down the database first by using the '-delete_db' command.")

if __name__ == "__main__":
    #Run This Code if Being Run From CLI
    import argparse

    #Do Argument Parsing
    parser = argparse.ArgumentParser(description="Perform Admin Commands against the Application", prog="Nastro")

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
                              version="%(prog)s r."+nastroVersionZ)
    
    parser.add_argument("--config",
                        help="The path to the config file required by the application",
                        default="config.json",
                        type=open,
                        action="store")

    args = parser.parse_args()
    #End Argument Parsing

    if args.create_new_db:
        createNewDB(config=args.config)
    elif args.version:
        report_version()

else:
    #Run This Code if Being Imported
    pass