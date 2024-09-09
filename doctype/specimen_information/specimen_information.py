# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SpecimenInformation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Literal["", "Local lab serial number", "Local lab sputum GeneXpert result", "Type of specimen Spot (S) Morning (M)", "Date specimen collected", "Date specimen Transported to PRL"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		typsp1: DF.Int
		typsp2: DF.Int
		typsp3: DF.Int
	# end: auto-generated types
	pass
