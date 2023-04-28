# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_data(filters):
    conditions = 'docstatus = 1'
    if filters.get('end'):
        conditions += f" AND posting_date BETWEEN '{(filters.get('start'))}' AND '{(filters.get('end'))}'"
    grp_class = frappe.db.sql(f"""
                              SELECT posting_date, name, customer_name, total
                              FROM `tabGym Subscription Invoice`
                              WHERE {conditions} 
                              ORDER BY posting_date""", as_dict=1)
    return grp_class



def get_columns():
    return [
		{
			"label": ("Posting Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 100,
		},
		{
			"label": ("Invoice No"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Gym Subscription Invoice",
			"width": 200,
		},
		{
			"label": ("Customer Name"),
			"fieldname": "customer_name",
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"label": ("Total Amount"),
			"fieldname": "total",
			"fieldtype": "Currency",
			"width": 100,
		}
	]