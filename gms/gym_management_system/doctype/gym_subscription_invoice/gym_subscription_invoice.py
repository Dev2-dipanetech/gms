# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

def get_amount(r=float,q=float):
	return (r * q)
def get_rate(sub_type, sub_name, month):
    if month == 1:
        return frappe.get_value(sub_type, sub_name, 'monthly_cost')
    else:
        return frappe.get_value(sub_type, sub_name, 'annual_cost')




class GymSubscriptionInvoice(Document):
    def before_save(self):
        if self.picked == 0:
            pass
        else :
            row = 0
            sum = 0
            for d in self.get('items'):
                row += 1
                if (d.monthly == 0) and (d.yearly == 0):
                    frappe.throw(f'Option not chosen in Row: {row}. Please choose either monthly or yearly')
                if (d.monthly == 1) and (d.yearly == 1):
                    frappe.throw(f'Both option chosen in Row: {row}. Please choose either monthly or yearly')
                d.rate = get_rate(d.subscription, d.sub_name, d.monthly)
                d.amount = get_amount(d.rate, d.quantity)
                sum += d.amount
            self.total = sum
            
            
    def before_submit(self):
        if self.picked == 0:
            frappe.throw("Subscription Details not filled completely. Please check subscription items again")
        else:
            for d in self.get('items'):
                if (d.monthly == 0) and (d.yearly == 0):
                    frappe.throw("Subscription Details not filled completely. Please check subscription items again")

                
                    
@frappe.whitelist()
def test_working(member,invoice):
    doc = frappe.get_doc('Gym Subscription Invoice',invoice)
    customer = frappe.get_doc('Gym Member',member)
    # child =[]
    sub_row = {'subscription':'Gym Membership','sub_name':customer.membership_subscription,'quantity': 1}
    doc.append('items',sub_row)
    # child.append(sub_row)
    if customer.locker_taken ==1:
        lock_row = {'subscription':'Gym Locker','sub_name':customer.locker_no,'quantity': 1}
        doc.append('items',lock_row)
    if customer.trainer_plan == 1:
        doc.append('items',{'subscription':'Other Gym Related Subscription','sub_name':'Professional Trainer','quantity':len(customer.trainer)})
    if customer.mem_grp_class:
        for d in customer.get('mem_grp_class'):
            doc.append('items',{
                'subscription':'Gym Group Class',
                'sub_name': d.gym_class,
                'quantity': 1
            })
    doc.picked = 1
    doc.save()
    return 'success'
