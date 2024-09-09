// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("demo", {
    onload:function(frm){
        let no=Math.random()*10
        frm.set_value("client_id",no)

    }
        



});
