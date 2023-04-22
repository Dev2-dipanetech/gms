# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymTrainer(Document):
    def before_save(self):
        if self.middle_name:
            self.full_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            self.full_name = self.first_name + ' ' + self.last_name