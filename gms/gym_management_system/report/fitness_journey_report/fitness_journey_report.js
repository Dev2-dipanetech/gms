// Copyright (c) 2023, Souradeep and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Fitness Journey Report"] = {
	"filters": [
		{
			"fieldname": "member",
			"label": "Member ID",
			"fieldtype": "Link",
			"options": "Gym Member",
			"width": 200
		}

	]
};
