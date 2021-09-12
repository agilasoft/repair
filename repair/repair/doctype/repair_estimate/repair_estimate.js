// Copyright (c) 2021, AgilaSoft Inc. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Repair Estimate', {
	refresh: function(frm) {
		frm.add_custom_button(__("Repair Order"), function() {
                        cur_frm.call('create_repair_order', function(r){});
                        cur_frm.refresh_fields(frm);
                }, __("Create"));
		frm.add_custom_button(__("Service Pack"), function() {
                        service_pack_dialog(frm);
                }, __("Add"));		
	}
});

frappe.ui.form.on("Repair Estimate Operation","charge_to", function(frm, cdt,cdn){
    var d = frappe.model.get_doc(cdt, cdn);
    frappe.call({
        method: 'repair.repair.doctype.repair_estimate.repair_estimate.get_rate',
        args:{
            'doc': frm.doc.name,
            'item': d.repair_operation,
            'billto': d.charge_to
        },
        callback: function(data) {
            if (!data.exc) {
                frappe.model.set_value(cdt, cdn, "rate", data.message);
            }
        },
    });
});

let service_pack_dialog = function(frm) {
	let dialog = new frappe.ui.Dialog({
		title: 'Add Service Pack',
		width: 100,
		fields: [
			{fieldtype: 'Link', label: 'Service Pack', fieldname: 'service_pack',
				options: 'Service Pack'
			}
		],
		primary_action_label: __('Add'),
		primary_action : function(){
			let service_pack = dialog.get_value('service_pack');
			frappe.call({
				doc: frm.doc,
				method: 'add_service_pack',
				args:{
					'service_pack': service_pack
				},
				callback: function(data) {
					if (!data.exc) {
						frm.reload_doc();
					}
				},
				freeze: true,
				freeze_message: __('Adding Service Pack Items')
			});
			frm.refresh_fields();
			dialog.hide();
		}
	});

	dialog.show();
};
