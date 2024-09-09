import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    data = get_data(filters)
    columns = get_columns()
    return columns, data

def get_columns():
    columns = [
        _("Form number") + ":Data:180",
        _("Name of Diagnostic Centre") + ":Data:180",
        _("Patients Name") + ":Data:180", 
        _("Date of Interview") + ":Data:180",
        _("District") + ":Data:130"
    ]
    return columns

def get_data(filters):
    condition=get_conditions(filters)
    
    query=f"""SELECT form_no,dcnam,patient_name,date_of_interview,dist from `tabTBR` where name is not null  {condition}""" 
    
    return frappe.db.sql(query,filters)

def get_conditions(filters):
    condition=''
    if filters.get("form_no"):
        condition += " and form_no = '{}'".format(filters.get("form_no"))
    
    if filters.get("patient_name"):
        condition +=" and patient_name ='{}'".format(filters.get("patient_name"))

    return condition
