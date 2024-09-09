# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Location(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		district: DF.Data | None
		form_number: DF.Int
		medical_officer: DF.Data | None
		pat_nam: DF.Data | None
		patient: DF.Link | None
		village: DF.Data | None
	# end: auto-generated types
	pass
