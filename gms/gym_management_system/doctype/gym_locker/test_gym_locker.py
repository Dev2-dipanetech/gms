# Copyright (c) 2023, Souradeep and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymLocker(FrappeTestCase):
    def test_gym_locker(self):
     test_locker = frappe.get_doc({
         "doctype": "Gym Locker",
         "assigned_to": "GM-0008"		 
	 }).insert()
