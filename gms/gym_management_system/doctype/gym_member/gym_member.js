// Copyright (c) 2023, Souradeep and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Member", {
	refresh:function(frm) {
        frm.set_query('locker_no',function(){
            return{
                filters: [
                    ['assigned_to','is','not set']
                ]
            }
        })

	},
});