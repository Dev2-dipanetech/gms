// Copyright (c) 2023, Souradeep and contributors
// For license information, please see license.txt

frappe.ui.form.on("Member Body Measurement", {
	onload:function(frm) {
        frm.set_value('posting_date', frappe.datetime.get_today());
        // frm.set_value('posting_time', frappe.datetime.get_time())

	},
});
