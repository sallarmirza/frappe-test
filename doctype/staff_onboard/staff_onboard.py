import frappe
from frappe.model.document import Document

class StaffOnboard(Document):
    def validate(self):
        # when dealing with a new doc
        stf = frappe.new_doc("staff")
        # appends your typed data
        stf.full_name = self.full_name
        stf.cinic = self.cinic
        stf.phone_number = self.phone_number
        stf.gender = self.gender
        stf.address = self.address

        # Adding degree rows by developer
        row = stf.append("degree", {})
        row.school = "abc"
        row.qualification = "Graduation"
        row.year_of_passing = "2020"

        row = stf.append("degree", {})
        row.school = "def"
        row.qualification = "MS"
        row.year_of_passing = "2021"
# end line script
        stf.save(ignore_permissions=True)
#--->        # frappe.db.commit()

    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        address: DF.LongText | None
        amended_from: DF.Link | None
        cinic: DF.Data | None
        full_name: DF.Data | None
        gender: DF.Literal["", "Male", "Female"]
        phone_number: DF.Phone | None
    # end: auto-generated types
