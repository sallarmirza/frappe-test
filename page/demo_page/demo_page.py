import frappe
@frappe.whitelist()
def get_data(date_of_birth=None):
    filters={}
    if date_of_birth:
        filters['date_of_birth'] = date_of_birth
    
    employee = frappe.db.get_value('Employee', filters)
    return employee
