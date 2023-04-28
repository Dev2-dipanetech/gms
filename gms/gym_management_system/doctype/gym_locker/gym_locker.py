# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymLocker(Document):
    def before_insert(self):
        if len(frappe.get_all('Gym Locker')) >= int(frappe.get_value('Gym Settings','Gym Settings','max_locker_no')):
            frappe.throw("Cannot make any more lockers. Ask the admin to change the 'maximum Number of lockers' in 'Gym Settings'")