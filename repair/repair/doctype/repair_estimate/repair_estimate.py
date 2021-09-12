# -*- coding: utf-8 -*-
# Copyright (c) 2021, AgilaSoft Inc. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import utils
from frappe.model.document import Document

class RepairEstimate(Document):
    pass
    
    @frappe.whitelist()
    def create_repair_order(self):
        doc = frappe.new_doc("Repair Order")
        doc.customer = self.customer
        doc.order_type = self.order_type
        doc.company = self.company
        doc.date = utils.now()
        doc.repair_estimate = self.name
        doc.appointment = self.appointment
        doc.billto_customer = self.billto_customer
        doc.billto_insurance = self.billto_insurance
        doc.billto_insurance = self.billto_insurance
        doc.customer_pl = self.customer_pl
        doc.insurance_pl = self.insurance_pl
        doc.warranty_pl = self.warranty_pl
        doc.currency = self.currency
        doc.conversion_rate = self.conversion_rate
        doc.selling_price_list = self.selling_price_list
        doc.price_list_currency = self.price_list_currency
        doc.plc_conversion_rate = self.plc_conversion_rate
        doc.operations = self.operations
        doc.spareparts = self.spareparts
        doc.tax_category = self.tax_category
        doc.taxes_and_charges = self.taxes_and_charges
        doc.taxes = self.taxes
        doc.payment_terms_template = self.payment_terms_template
        doc.payment_schedule = self.payment_schedule
        doc.tc_name = self.tc_name
        doc.terms = self.terms
        doc.campaign = self.campaign
        doc.source = self.source
        doc.status = self.status
        doc.supplier_quotation = self.supplier_quotation
        doc.insert()
        
        frappe.msgprint(doc.name + " was successfully created.")

    @frappe.whitelist()
    def add_service_pack(self, service_pack):
        sp = frappe.db.sql("""SELECT * FROM `tabService Pack Operation`
            WHERE parent = %s
            """, (service_pack), as_dict=1)
        
        for i in sp:
            op = frappe.get_doc("Item", i.repair_operation)
            self.append("operations",
                {
                    'repair_operation': op.name,
                    'description': op.description,
                    'item_name': op.item_name,
                    'uom': i.uom,
                    'qty': op.standard_qty
                })
            
            spareparts = frappe.db.sql("""SELECT * FROM `tabRepair Operation Sparepart`
                WHERE parent = %s""", (i.repair_operation), as_dict=1)

            for p in spareparts:
                self.append("spareparts",
                    {
                        'operation': i.repair_operation,
                        'item_code': p.item,
                        'item_name': p.item_name,
                        'description': p.item_name,
                        'stock_uom': p.uom,
                        'uom': p.uom,
                        'stock_qty': p.qty,
                        'qty': p.qty
                    })

@frappe.whitelist()                    
def get_rate(doc, item, billto):
    if billto == "Customer":
        rate = frappe.db.sql("""SELECT price_list_rate FROM `tabRepair Estimate` e, `tabItem Price` p
            WHERE e.customer_pl = p.price_list AND p.item_code = %s AND e.name = %s""", 
            (item, doc), as_dict=1)
        for r in rate:
            return r.price_list_rate
        else:
            frappe.throw("No Pricelist found.")
    
    if billto == "Insurance":
        rate = frappe.db.sql("""SELECT price_list_rate FROM `tabRepair Estimate` e, `tabItem Price` p
            WHERE e.insurance_pl = p.price_list AND p.item_code = %s AND e.name = %s""", 
            (item, doc), as_dict=1)
        for r in rate:
            return r.price_list_rate
        else:
            frappe.throw("No Pricelist found.")
    
    if billto == "Warranty":
        rate = frappe.db.sql("""SELECT price_list_rate FROM `tabRepair Estimate` e, `tabItem Price` p
            WHERE e.warranty_pl = p.price_list AND p.item_code = %s AND e.name = %s""", 
            (item, doc), as_dict=1)
        for r in rate:
            return r.price_list_rate
        else:
            frappe.throw("No Pricelist found.")
           