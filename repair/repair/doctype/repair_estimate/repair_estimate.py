# -*- coding: utf-8 -*-
# Copyright (c) 2021, AgilaSoft Inc. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RepairEstimate(Document):
    pass
    
    @frappe.whitelist()
    def create_repair_order(self):
        return 0
    
    def test_me(self):
        return 0