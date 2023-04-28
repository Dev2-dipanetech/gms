# Copyright (c) 2023, Souradeep and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns= get_columns()
    data = get_data(filters)
    return columns, data

def get_data(filters):
    conditions = '1=1'
    if filters.get('member'):
        conditions += f" AND member = '{filters.get('member')}'"
    query = f"""
        SELECT 
            mbm.posting_date,
            mbm.member,
            mbm.member_name,
            mbm.height,
            mbm.weight,
            mbm.bmi,
            mbm.caloriesin_kcal,
            mbm.chest,
            mbm.upper_arm,
            mbm.waist,
            mbm.hips,
            mbm.thigh
        FROM `tabMember Body Measurement` as mbm
        WHERE {conditions}
        ORDER BY mbm.posting_date
        """
    data = frappe.db.sql(query)
    return data


def get_columns():
    return [
        "Posting Date:Date:100",
        "Member ID:Link/Gym Member:100",
        "Name:Data:150",
        "Height:Float:75",
        "Weight:Float:75",
        "BMI:Float:75",
        "Calories Intake:Float:150",
        "Chest(in cm):Float:125",
        "Upper Arm(in cm):Float:125",
        "Waist(in cm):Float:95",
        "Hips(in cm):Float:95",
        "Thigh(in cm):Float:95"
    ]