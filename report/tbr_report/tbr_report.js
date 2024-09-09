// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["tbr report"] = {
	"filters": [
		{
			"fieldname":"dist",
			"label":__("Name of District"),
			"fieldtype":"Data"
		},{
			"fieldname":"patnam",
			"label":__("Patient Name"),
			"fieldtype":"Data"
		}

	]
};
