# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TBR(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.test.doctype.specimen_information.specimen_information import SpecimenInformation
		from frappe.types import DF

		advise: DF.Literal["", "X-ray", "Blood test", "Skin Test", "Other"]
		age: DF.Int
		amended_from: DF.Link | None
		attdugy: DF.Literal["", "No", "Yes"]
		bldcoug: DF.Literal["", "Yes", "No"]
		chstpnl: DF.Literal["", "Yes", "No"]
		cluster_code: DF.Int
		coug: DF.Literal["", "Yes", "No"]
		dcnam: DF.Data
		dist: DF.Data | None
		dolt: DF.Data | None
		education: DF.Literal["", "No schooling", "Primary school, not completed", "Primary school, completed", "Secondary school, not completed", "Secondary school, completed", "Further education after secondary school"]
		emplmnt: DF.Literal["", "Government employee", "Private employee", "Self employed", "Pupil/student", "Housewife", "Unemployed", "Other"]
		famlymem: DF.Int
		fevrnit: DF.Literal["", "Yes", "No"]
		fhusnam: DF.Data | None
		fmno: DF.Int
		for_how_long_did_you_wait_before_seeking_health_care: DF.Data | None
		fourcode: DF.Data | None
		hftrets: DF.Literal["", "Basic Health Unit", "Rural Health Center", "Tehsil HQ Hospital", "District HQ Hospital", "TB Centre", "Private practitioner", "Traditional healer", "Pharmacy", "Other", "None"]
		hlrectr: DF.Literal["", "Less than a month", "1 to 2 months", "6 to 8 months", "Others"]
		hlsick: DF.Data | None
		hlys: DF.Data | None
		hubptb: DF.Literal["", "Yes", "No"]
		idpe: DF.Literal["", "No", "Yes"]
		injim: DF.Literal["", "No", "Yes"]
		intdate: DF.Date
		istemp3: DF.Literal["", "Business", "Shop keeping", "Farming", "Office work", "Teacher", "Manual labour", "Other"]
		losapt: DF.Literal["", "Yes", "No"]
		loswty: DF.Literal["", "Yes", "No"]
		mdicphar: DF.Literal["", "Yes", "No"]
		mhtong: DF.Literal["", "Punjabi", "Sindhi", "Bolochi", "Pushtoon", "Saraiki", "Kashmiri", "Urdu Speaking", "Other"]
		mo: DF.Data | None
		mobnum: DF.Phone | None
		moninicms: DF.Int
		mosigdat: DF.Date | None
		nitswet: DF.Literal["", "Yes", "No"]
		nmattdrg: DF.Data | None
		othsymp: DF.Literal["", "Yes", "No"]
		otptret: DF.Data | None
		patnam: DF.Data
		patregtbm: DF.Literal["", "No", "Yes"]
		plotcom: DF.Literal["", "Cured", "Treatment completed", "Loss to follow up", "Failure", "Transfer out"]
		publichf: DF.Literal["", "Public Health Sector"]
		rpttb: DF.Literal["", "No", "Yes"]
		sex: DF.Literal["", "Male", "Female", "Not Recorded"]
		smok: DF.Literal["", "Yes", "No"]
		smoky: DF.Int
		specimen_id_information: DF.Table[SpecimenInformation]
		spexp: DF.Literal["", "No", "Yes"]
		spucoug: DF.Literal["", "Yes", "No"]
		sspe: DF.Literal["", "No", "Yes"]
		tbreg: DF.Data | None
		tbtmo: DF.Literal["", "No", "Yes"]
		tcnum: DF.Phone | None
		tmom: DF.Literal["", "No", "Yes"]
		toutcom: DF.Literal["", "Cured", "Not Cured", "Unknown"]
		tretrec: DF.Literal["", "No", "Yes"]
		vcity: DF.Data | None
		watkt: DF.Literal["", "Pills and Injections", "Pills only", "Injections only", "Don't Remember"]
		when_you_first_felt_sick: DF.Data | None
		whomt: DF.Literal["", "Doctor", "Nurse", "Pharmacist", "Traditional Healer", "Other"]
		whpttbn: DF.Literal["", "less then one year", "between 1 to 2 years", "betweeen 2 to 5 years", "more then 5 years"]
		whpttby: DF.Literal["", "Yes", "No"]
		wtbt: DF.Literal["", "Public Sector", "Private Sector", "Other. Please"]
		wvfpill: DF.Int
		xryexp: DF.Literal["", "No", "Yes"]
	# end: auto-generated types
	pass
