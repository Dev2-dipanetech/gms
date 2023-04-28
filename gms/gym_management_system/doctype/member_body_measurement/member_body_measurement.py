# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now


class MemberBodyMeasurement(Document):
    def before_save(self):
        self.bmi = (self.weight)/((self.height)**2)
        self.height_in_foot = 3.28084 * self.height
        self.weight_in_pounds = 2.20462 * self.weight
        if self.bmi <=18.5:
            self.weight_status = 'Underweight'
        if (self.bmi >18.5) and (self.bmi <=24.9):
            self.weight_status = 'Healthy'
        if (self.bmi >24.9) and (self.bmi <=29.9):
            self.weight_status = 'Overweight'
        if (self.bmi >30):
            self.weight_status = 'Obese'