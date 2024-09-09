# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	data=get_data(filters)
	columns=get_columns()
	return columns, data

def get_columns():
    columns=[
        _("Patient Name")+":Data:180",
		_("District")+":Data:180",
		_("Form no")+ ":Data:180",
        
	]
    return columns

def get_data(filters):
    conditions=get_conditions(filters)
    query=f"""SELECT patnam,dist,fmno from `tabTBR` where patnam is not null {conditions}"""
    return frappe.db.sql(query)

def get_conditions(filters):
    conditions=''
    if filters.get("patnam"):
        conditions+="and patnam='{}'".format(filters.get("patnam"))
    if filters.get("dist"):
        conditions+="and dist='{}'".format(filters.get("dist"))
    return conditions
    