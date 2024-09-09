// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["TBR Info"] = {
	"filters": [
		{
			"fieldname":"dcnam",
			"label":__("Name of Diagnostic Centre"),
			"fieldtype":"Data",
			// "options":"",
			"reqd":1

		},
		{
			"fieldname":"form_no",
			"label":__("Form number"),
			"fieldtype":"Data",
		},
		{
			"fieldname":"patient_name",
			"label":__("Patient Name"),
			"fieldtype":"Data",
		},{
			"fieldname":"date_of_interview",
			"label":__("Date of Interview"),
			"fieldtype":"Data",
		},{
			"fieldname":"dist",
			"label":__("District"),
			"fieldtype":"Data",
		}
		

	]
};
