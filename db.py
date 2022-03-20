# External Imports
import sqlalchemy as sa
import sqlalchemy.orm
import json
import socket

# Internal Imports
from __version__ import *
global nastroVersion, nastroVersionZ

if __name__ == "__main__":
    raise "This Cannot be Called from a Command Line. Please Import this Module correctly."
else:
    Base = sqlalchemy.orm.declarative_base()

    class Admin(Base):
        __tablename__ = "admin"

        admin_id = sa.Column(
                            sa.Boolean(),
                            primary_key=True)
        admin_version = sa.Column(
                            sa.Integer(),
                            nullable=False)
        admin_hostname = sa.Column(
                            sa.String(128),
                            nullable=False)
        admin_user_cred = sa.Column(
                            sa.String(64),
                            nullable=False)

    class Audit(Base):
        __tablename__ = "audit"

        audit_id = sa.Column(
                            sa.Integer(),
                            primary_key=True,
                            autoincrement=True)
        audit_version = sa.Column(
                            sa.Integer(),
                            nullable=False)
        audit_hostname = sa.Column(
                            sa.String(128),
                            nullable=False)
        audit_timestamp = sa.Column(
                            sa.Integer(),
                            nullable=False,
                            server_default=sa.func.now())
        audit_action = sa.Column(
                            sa.JSON(),
                            nullable=False)
        audit_count = sa.Column(
                            sa.Integer(),
                            nullable=False)

    class Tape(Base):
        __tablename__ = "tape"

        tape_barcode = sa.Column(
                            sa.String(8),
                            primary_key=True)
        tape_location = sa.Column(
                            sa.String(6),
                            sa.ForeignKey("location.location_id"),
                            nullable=False)
        tape_destroyed = sa.Column(
                            sa.Boolean,
                            nullable=False)
        tape_type = sa.Column(
                            sa.String(8),
                            nullable=False)
        tape_barcode_trunc = sa.Column(
                            sa.String(6),
                            nullable=False)
        tape_scratch = sa.Column(
                            sa.Boolean,
                            nullable=False)
        tape_library = sa.Column(
                            sa.String(16),
                            sa.ForeignKey("library.library_id"),
                            nullable=False)
        tape_software = sa.Column(
                            sa.String(16))
        tape_slot = sa.Column(
                            sa.Integer())

        tape_detail = sa.orm.relationship(
                            "Tape_Details", cascade="all, delete, delete-orphan")

    class Tape_Details(Base):
        __tablename__ = "tape_details"

        tape_barcode = sa.Column(
                            sa.String(8),
                            sa.ForeignKey("tape.tape_barcode"),
                            primary_key=True)
        tape_description = sa.Column(
                            sa.String(512))
        tape_condition = sa.Column(
                            sa.String(64),
                            nullable=False)
        tape_serial = sa.Column(
                            sa.String(32))
        tape_manufacturer = sa.Column(
                            sa.String(16))
        tape_encryption_key = sa.Column(
                            sa.String(128))
        tape_hash = sa.Column(
                            sa.String(256))

    class Library(Base):
        __tablename__ = "library"

        library_id = sa.Column(
                            sa.String(16),
                            primary_key=True)
        library_display_name = sa.Column(
                            sa.String(64),
                            nullable=False)
        library_location = sa.Column(
                            sa.String(6),
                            sa.ForeignKey("location.location_id"),
                            nullable=False)
        library_model = sa.Column(
                            sa.String(32))
        library_manufacturer = sa.Column(
                            sa.String(32))
        library_slots = sa.Column(
                            sa.Integer(),
                            nullable=False)
        library_ip = sa.Column(
                            sa.String(48))
        library_user_cred = sa.Column(
                            sa.String(64))
        library_user_pass = sa.Column(
                            sa.String(64))

    class Location(Base):
        __tablename__ = "location"

        location_id = sa.Column(
                            sa.String(6),
                            primary_key=True)
        location_display_name = sa.Column(
                            sa.String(64),
                            nullable=False)
        location_address = sa.Column(
                            sa.String(128))
        location_vault = sa.Column(
                            sa.String(32))
        location_slots = sa.Column(
                            sa.Integer())

    config = json.load(open("config.json"))

    #priamry_engine = sa.engine_from_config(config["primary_database"],prefix="db")                                 #Create from Config (Not functional?)
    primary_engine = sa.create_engine("sqlite+pysqlite:///test.db", echo=True, future=True, pool_pre_ping=True)     #Create a File
    #primary_engine = sa.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True, pool_pre_ping=True)   #Create it in memory