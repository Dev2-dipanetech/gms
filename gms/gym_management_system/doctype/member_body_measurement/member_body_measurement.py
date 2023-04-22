# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now


class MemberBodyMeasurement(Document):
    def before_save(self):
        if not self.first_measurement_date:
            self.first_measurement_date = now()
        
        for s in self.get('bmi'):
            s.bmi = (s.weight)/((s.height)**2)
            if s.bmi <=18.5:
                s.weight_status = 'Underweight'
            if (s.bmi >18.5) and (s.bmi <=24.9):
                s.weight_status = 'Healthy'
            if (s.bmi >24.9) and (s.bmi <=29.9):
                s.weight_status = 'Overweight'
            if (s.bmi >30):
                s.weight_status = 'Obese'