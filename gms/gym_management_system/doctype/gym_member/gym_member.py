# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
    
class GymMember(WebsiteGenerator):
    def before_save(self):
        if self.middle_name:
            self.full_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            self.full_name = self.first_name + ' ' + self.last_name