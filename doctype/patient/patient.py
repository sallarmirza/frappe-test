# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Patient(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		district: DF.Data | None
		father_name: DF.Data | None
		name1: DF.Data | None
		patient_id: DF.Data | None
		tbr: DF.Link | None
	# end: auto-generated types
	pass
