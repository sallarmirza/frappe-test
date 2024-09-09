# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Employee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		date_of_birth: DF.Date | None
		emp_id: DF.Data | None
		father_name: DF.Data | None
		gender: DF.Literal["", "Male", "Female"]
		name1: DF.Data | None
	# end: auto-generated types
	pass
