# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymClassAttendance(Document):
    def before_save(self):
        if self.get('attendance_details'):
            row = 0
            sum = 0
            for d in self.get('attendance_details'):
                sum += d.rating
                row += 1
            self.average_rating = sum/row
