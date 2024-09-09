# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	data=get_data()
	columns=get_col()
	return columns, data

def get_col():
    columns=[
		_("Employee Name")+":Data:160",
		_("Gender")+":Data:120",
		_("Name of Course")+":Data:150",
		_("Course Id")+":Data:150",        
	]
    return columns

def get_data():
    query = """
        SELECT emp.name1, emp.gender, Es.course_name, Es.user
        FROM `tabEnroll Courses` AS Es
        INNER JOIN `tabEmployee` AS emp ON Es.user = emp.name
    """
    result = frappe.db.sql(query, as_dict=True)
    new_list = []

    for row in result:
        user = row['user']
        existing_row = next((item for item in new_list if item['user'] == user), None)

        if existing_row:
            existing_row['course_name'] += f", {row['course_name']}"
        else:
            new_list.append({
                'name1': row['name1'],
                'gender': row['gender'],
                'course_name': row['course_name'],
                'user': row['user']
            })

    formatted_list = []
    for item in new_list:
        formatted_list.append([
            item['name1'],         
            item['gender'],        
            item['course_name'],   
            item['user']           
        ])

    return formatted_list
