from datetime import datetime
import frappe
from frappe.model.document import Document

class TDR(Document):
    # def validate(self):
    #     start_date = datetime(2024, 1, 1)
    #     last_date = datetime(2025, 9, 30)
    #     selected_date = self.intdate
        
    #     if selected_date and start_date <= selected_date <= last_date:
            
    #         pass
    #     else:
    #         frappe.msgprint("Please select a date between January 1, 2024, and September 30, 2025.")
    #         self.intdate = None 
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.
    
    from typing import TYPE_CHECKING
    
    if TYPE_CHECKING:
        from frappe.types import DF
        
        age: DF.Int
        amended_from: DF.Link | None
        countnum: DF.Data | None
        culscod: DF.Int
        dcnam: DF.Data | None
        dist: DF.Data | None
        fhusnam: DF.Data | None
        fmno: DF.Int
        fourcode: DF.Data | None
        intdate: DF.Data | None
        mobnum: DF.Data | None
        patnam: DF.Data | None
        sex: DF.Literal["", "Male", "Female", "Not Recorded"]
        tbreg: DF.Data | None
        vcity: DF.Data | None
    # end: auto-generated types
