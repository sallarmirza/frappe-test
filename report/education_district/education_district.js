// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["Education District"] = {
	"filters": [
		{
			"fieldname": "district",
			"fieldtype": "Table MultiSelect",
			"label": "District",
			"options": "District Names"
	   }
		

	]
};
