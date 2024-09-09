# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	data=get_data()
	columns=get_columns()
	return columns, data

def get_columns():
    columns=[
		_("Name of Patient")+":Data:150",
		_("Father Name")+ ":Data:150",
		_("District")+ ":Data:150,"
	]
    return columns

def get_data():
	query="SELECT pt.name1,pt.father_name,pt.district from `tabPatient` as pt join `tabTBR` as tbr On pt.name1=tbr.patnam"
	return frappe.db.sql(query);

    