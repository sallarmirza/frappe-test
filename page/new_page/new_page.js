frappe.pages['new-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Education',
		single_column: true
	});
	$(frappe.render_template("new_page", {})).appendTo(page.main);
    $.getScript("https://code.highcharts.com/highcharts.js",function(){
    createChart();
    })
    filters.add(page);
}
filters = {
    add: async function(page) {
        
        // name1= page.add_field({
        //     label: "Name",
        //     fieldtype: "Data",
        //     fieldname: "name1"
        // });

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
        method: "frappe.test.page.new_page.new_page.get_data",
        args: {
            // name1: page.fields_dict.name1.get_value(),
            
        },
        freeze: true,
        callback: function(r) {
            if (r.message) {
                let x=r.message
                console.log("x",x)
                // frappe.msgprint(` Total: ${r.message}`);

                createChart(x)
            } else {
                frappe.msgprint("No Person found with the given details.");
            }
        }
    });
}
function createChart(x){
    Highcharts.chart('container', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Qualification'
        },
        tooltip: {
            valueSuffix: '%'
        },
        plotOptions: {
            series: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: [{
                    enabled: true,
                    distance: 30
                }, {
                    enabled: true,
                    distance: -40,
                    format: '{point.percentage:.1f}%',
                    style: {
                        fontSize: '1.2em',
                        textOutline: 'none',
                        opacity: 0.7
                    },
                    filter: {
                        operator: '>',
                        property: 'percentage',
                        value: 10
                    }
                }]
            }
        },
        series: [
            {
                name: 'Percentage',
                colorByPoint: true,
                data: [
                    {
                        name: 'Graduation',
                        y:x[0][1]
                    },
                    {
                        name: 'MS',
                        y: x[1][1]
                    },
                    {
                        name: 'PHD',
                        sliced: true,
                        selected: true,
                        y: x[2][1]
                    },
                    
                ]
            }
        ]
    });    
}
