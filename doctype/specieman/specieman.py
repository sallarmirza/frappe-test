# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Specieman(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		specimen_1: DF.Literal["", "Local lab Serial Number", "Local Lab sputum GeneXpert result", "Type of specimen collected", "Date specimen Transported to PRL"]
		specimen_2: DF.Literal["", "Local lab Serial Number", "Local Lab sputum GeneXpert result", "Type of specimen collected", "Date specimen Transported to PRL"]
		specimen_3: DF.Literal["", "Local lab Serial Number", "Local Lab sputum GeneXpert result", "Type of specimen collected", "Date specimen Transported to PRL"]
	# end: auto-generated types
	pass
