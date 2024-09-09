frappe.pages['demo-page'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Demo Page',
        single_column: true
    });
    $(frappe.render_template("demo_page", {})).appendTo(page.main);
    filters.add(page, wrapper);
}

filters = {
    add: async function(page, wrapper) {
     
        date_of_birth = page.add_field({
            label: "Date of Birth",
            fieldtype: "Date",
            fieldname: "date_of_birth"
        });

        page.add_field({
            label: "View",
            fieldtype: "Button",
            fieldname: "filter",
            async click() {
                server_call(page);
            }
        });
    },
};

function server_call(page) {
   
    frappe.call({
        method: "frappe.test.page.demo_page.demo_page.get_data",
        args: {
            date_of_birth: page.fields_dict.date_of_birth.get_value()
        },
        freeze: true,
        callback: function(r) {
            if (r.message) {
                frappe.msgprint(`Employee Name: ${r.message}`);
            } else {
                frappe.msgprint("No employee found with the given details.");
            }
        }
    });
}
