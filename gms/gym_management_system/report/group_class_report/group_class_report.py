# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data

# Group Class Name
# No of Booking
# Average Rating

def get_columns():
    return [
		{
			"label": ("Group Class"),
			"fieldname": "class_name",
			"fieldtype": "Link",
			"options": "Gym Group Class",
			"width": 200,
		},
		{
			"label": ("Number of Bookings"),
			"fieldname": "no_book",
			"fieldtype": "Int",
			"width": 150,
		},
		{
			"label": ("Average Rating"),
			"fieldname": "avg_rating",
			"fieldtype": "Rating",
			"width": 200,
		}
	]

def get_data():
    grp_class = frappe.db.sql("""
                              SELECT class_name
                              FROM `tabGym Group Class`""", as_dict=1)
    for grp in grp_class:
        query = f"""SELECT average_rating FROM `tabGym Class Attendance` WHERE class = '{grp.class_name}'"""
        rating = frappe.db.sql(query,as_list =1)
        sum = 0
        row = 0
        grp.no_book = 0
        
        for rt in rating:
            sum += rt[0]
            # frappe.throw(str(rt[0]))
            row += 1
        if row == 0:
            grp.avg_rating = 0
        else:
            grp.avg_rating = (sum/row)
        group_class = frappe.get_doc('Gym Group Class', grp.class_name)
        grp.no_book = len(group_class.get("class_subscribers"))
        
    return grp_class
