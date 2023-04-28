// Copyright (c) 2023, Souradeep and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Revenue Report"] = {
	"filters": [
		{
			"fieldname": "start",
			"label": "Start Date",
			"fieldtype": "Date",
			"width": 200
		},
		{
			"fieldname": "end",
			"label": "End Date",
			"fieldtype": "Date",
			"width": 200
		}

	]
};
