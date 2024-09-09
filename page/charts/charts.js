frappe.pages['charts'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Chart',
		single_column: true
	});
	$(frappe.render_template("charts",{})).appendTo(page.main)
	filters.add(page,wrapper)
}
filters={
	add:async function(page,wrapper) {
		let patnam=page.add_field({
			labal:"Patient Name",
			fieldtype:"Data",
			fieldname:"patnam"
		})
		
	}
}