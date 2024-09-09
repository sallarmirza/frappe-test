# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Education(Document):
	def before_save(self):
		doc = frappe.get_doc('Education','37')
		# frappe.throw(doc.name1)
		self.name1=doc.name1
		self.age=doc.age
		for doc in doc.degree:
			for x in self.degree:
				x.school=doc.school
			frappe.msgprint(_(doc.school))
			frappe.msgprint(_(doc.qualification))
		doc.save(ignore_permissions=True)
		 
		pre_doc=frappe.new_doc('Education')
		pre_doc.name1='ABc'
		pre_doc.age='21'
		for pre_doc in pre_doc.degree:
			pre_doc.school='new school'
			pre_doc.qualification='MS'
			pre_doc.year_of_passing=2020



	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.core.doctype.degree.degree import Degree
		from frappe.test.doctype.district_names.district_names import DistrictNames
		from frappe.types import DF

		age: DF.Data | None
		amended_from: DF.Link | None
		degree: DF.Table[Degree]
		district: DF.TableMultiSelect[DistrictNames]
		name1: DF.Data | None
		verified_districts: DF.Link | None
	# end: auto-generated types
	pass
