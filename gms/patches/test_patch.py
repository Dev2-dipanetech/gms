import frappe

def execute():
    ls = frappe.get_list(doctype = 'Gym Locker')
    
    for d in ls:
        doc = frappe.get_doc('Gym Locker',d.name)
        doc.test_patch_data = "HELLO"
        doc.save()
    