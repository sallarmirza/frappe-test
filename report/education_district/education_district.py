# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_col()
	data=get_data(filters)
	return columns, data

def get_col():
    columns=[
		_("Student Name")+":Data:150",
		_("Qualification")+":Data:150",
		_("District")+":Data:150",
	]
    return columns

def get_data(filters):
    condition=get_conditions(filters)
    query=f"""Select edu.name1,deg.qualification,dt.name from `tabEducation` as edu join `tabDegree`  as deg join `tabDistrict` as dt {condition}"""
    return frappe.db.sql(query)

def get_conditions(filters):
    condition=''
    if filters.get('district'):
        # in, = are operators
        condition+="and district in'{}'".format(filters.get("district"))
    # frappe.throw(f"filters used={filters.get('district')}")
    # district in ("Islamabad", "Lahore")
    return condition