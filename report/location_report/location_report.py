# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data()
	return columns, data

def get_columns():
    columns=[
        _("Patient Name")+ ":Data:150",
		_("Village")+ ":Data:150",
		_("District")+ ":Data:150",
	]
    return columns

def get_data():
    query="select pat_nam,village,district from `tabLocation`"
    return frappe.db.sql(query)