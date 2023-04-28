import frappe

def execute():
    from frappe.database import db

    # Make changes to the database schema
    db.sql("ALTER TABLE `tabGym Locker` ADD COLUMN `my_new_field` varchar(255);")
