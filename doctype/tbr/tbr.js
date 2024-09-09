// Copyright (c) 2024, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("TBR", {
	refresh(frm) {
        // cluster code
        let cluster_code=Math.random()*(25-1)*2;
        let clustcode=Math.floor(cluster_code)
        frm.set_value("cluster_code",clustcode)
        // fmno
        let fmno=Math.random()*(1000-7)*2;
        let formv=Math.floor(fmno);
        frm.set_value("fmno",formv);
        let culcode=clustcode.toString();
        let frmv=formv.toString();
        // 4-digit code
        let fourcode=frmv.concat("-",culcode);
        frm.set_value("fourcode",fourcode);
        // datepicker 
        frm.fields_dict.intdate.datepicker.update({
            minDate: new Date('2024-01-01'),
            maxDate: new Date('2025-09-30')
        });
	},
    validate:function(frm){
        let dist=frm.doc.dist;
        let distregx=/^[^.]+$/g;
        if(!distregx.test(dist)){
            frappe.msgprint(__("Cannot Enter dot"));
            frappe.validated=false;
        }
        let tbreg=frm.doc.tbreg;
        let tbregreg=/^[^.]+$/g;
        if(!tbregreg.test(tbreg)){
            frappe.msgprint(__("Cannot Enter dot in Registration Number"))
            frappe.validated=false;
        }
        let patnam=frm.doc.patnam
        let patnamregex=/^([^0-9]*)$/;
        if(!patnamregex.test(patnam) ){
            frappe.msgprint(__("Name must only have Alphabets"))
            frappe.validated=false;
           
            
        }
        if(patnam.length<4){
            frappe.msgprint(__("Name must have more than 3 characters"))
            frappe.validated=false;
            
        }
        let fhusnam=frm.doc.fhusnam
        let fhusnamregex=/^([^0-9]*)$/;
        if(!fhusnamregex.test(fhusnam) ){
            frappe.msgprint(__("Name must only have Alphabets"))
            frappe.validated=false;
            
        }
        // if(fhusnam.length<4){
        //     frappe.msgprint(__("Name must have more than 3 characters"))
        //     frappe.validated=false;
            
        // }
        
    },
    patregtbm:function(frm){
        if(frm.doc.patregtbm=="Yes"){
            let value="Yes"
            frm.set_value("dolt",value);
        }else{
            let value2="No"
            frm.set_value("dolt",value2);
        }
    },
    plotcom:function(frm){
        console.log("hello1")
        console.log(frm.doc.plotcom);
        
        if(frm.doc.plotcom=="Cured"){
            let v1="Cured"
            
        console.log("cured")
            frm.set_value("otptret",v1);
        }
       if(frm.doc.plotcom=="Treatment completed"){
            let v2="Treatment completed";
            console.log("hi");
            
            frm.set_value("otptret",v2);
            
        console.log("TC")
        }else if(frm.doc.plotcom=="Loss to follow up"){
            let v3="Loss to follow up";
            frm.set_value("otptret",v3);
            
        console.log("Folow up")

        }else if(frm.doc.plotcom=="Failure"){
            let v4="Failure";
            frm.set_value("otptret",v4);
            
            console.log("fail")
        }else if(frm.doc.plotcom=="Transfer out"){
            let v5="Transfer out";
            frm.set_value("otptret",v5);
        }
    }
    
});
