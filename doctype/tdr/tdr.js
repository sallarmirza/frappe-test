frappe.ui.form.on("TDR", {
    refresh: function(frm) {
        let minDate = new Date("2024-01-01");
        let maxDate = new Date("2025-09-30");
        
        let today = new Date(frappe.datetime.get_today());
    
        frm.fields_dict.intdate.$input.datepicker({
            minDate: minDate,
            maxDate: maxDate
        });
    
        if (frm.doc.intdate) {
            let selectedDate = new Date(frm.doc.intdate);
            if (selectedDate < minDate || selectedDate > maxDate) {
                frappe.msgprint("Please select a date between January 1, 2024, and September 30, 2025.");
                frm.set_value("intdate", null);  // Clear the field if the date is out of range
            }
        }
    },
    
    age:function(frm){
        if(frm.doc.age>99){
            frm.msgprint(__("Can't store age greater than 98"))
        }
    },
    onload_post_render:function(frm){
        const count=Math.random()*(100-2)*2;
        let fmno=Math.floor(count)+1;
        frm.set_value("fmno",fmno);
        let culscod=Math.random()*(50-2)*1;
        frm.set_value("culscod",Math.floor(culscod));
        let newfm=Math.floor(count).toString();
        let newcols=Math.floor(culscod).toString();
        let fourcode=newcols.concat("-",newfm);
        frm.set_value("fourcode",fourcode);
    }
    
});
