// Copyright (c) 2020, asdf and contributors
// For license information, please see license.txt

frappe.ui.form.on('URP Tenant', {
	before_tenants_ref_remove: function(frm, dct, dcn) {
        frappe.throw(__("Tenants may not be removed from table.  Close the tenant by opening the record, then checking the 'Close tenant' checkbox."));
	}
});