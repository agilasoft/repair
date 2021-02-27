# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
            "module_name": "Repair",
            "category": "Modules",
            "label": _("Repair"),
            "color": "#FFF5A7",
            "reverse": 1,
            "icon": "octicon octicon-tools",
            "type": "module",
            "description": "Create estimates, orders, and billings for your repairs."
		},
	]
