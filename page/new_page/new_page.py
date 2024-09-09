import frappe
@frappe.whitelist()
def get_data(name1=None):
    # filters={}
    # if name1:
    #     filters['name1'] = name1
    query="""SELECT qualification,COUNT(*) AS count
    FROM `tabDegree`
    WHERE qualification IN ('Graduation', 'MS', 'PhD')
    GROUP BY qualification;
    """
    education = frappe.db.sql(query)
    return education
