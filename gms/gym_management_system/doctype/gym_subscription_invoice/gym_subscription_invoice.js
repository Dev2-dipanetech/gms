// Copyright (c) 2023, Souradeep and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Subscription Invoice", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Gym Subscription Invoice", "get_child", function(frm) { 
    // console.log(frm.doc.customer)
    frappe.call({
        method: 'gms.gym_management_system.doctype.gym_subscription_invoice.gym_subscription_invoice.test_working',
        args: {'member':frm.doc.customer,
                'invoice':frm.docname,
    },
    callback: function(r) {
      // show success message
      frappe.show_alert('Subscription(s) Added Successfully', 5);

      // reload the current form
      cur_frm.reload_doc();
    }
    });
    

});


frappe.ui.form.on("Gym Subscription Invoice", {
	onload:function(frm) {
        frm.set_value('posting_date', frappe.datetime.get_today());
        // frm.set_value('posting_time', frappe.datetime.get_time())

	},
});
