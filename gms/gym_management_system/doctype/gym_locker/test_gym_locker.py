# Copyright (c) 2023, Souradeep and Contributors
# See license.txt

import frappe
# import frappe.defaults

from frappe.tests.utils import FrappeTestCase
class TestEvent(FrappeTestCase):
    
    def test_another(self):
        frappe.set_user("Administrator")
        doc = frappe.get_doc({
            "doctype": "Gym Locker",
            "locker_no":"123",
            # "assigned_to": "GM-0008",
            "annual_cost": 1000,
            "monthly_cost": 100,
            "volume": 'Small'
        }).insert()
        
    def test_2(self):
        frappe.set_user("Administrator")
        doc = frappe.new_doc('Gym Locker')
        doc.locker_no = "5555"
        doc.annual_cost = 1056.33
        doc.monthly_cost = 12.33
        doc.insert()
        
 