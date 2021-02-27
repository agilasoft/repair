from __future__ import unicode_literals
from frappe import _

def get_data():

        return [
            {
                    "label": _("Front Office"),
                    "icon": "icon-file",
                    "items": [
                    {
                            "type": "doctype",
                            "name": "Repair Schedule",
                            "label": _("Repair Schedule"),
                    },
                    {
                            "type": "doctype",
                            "name": "Estimate",
                            "label": _("Estimate"),
                    },
                    {
                            "type": "doctype",
                            "name": "Repair Order",
                            "label": _("Repair Order"),
                    },
                    {
                            "type": "doctype",
                            "name": "Insurance Claim",
                            "label": _("Insurance Claim"),
                    },
                    {
                            "type": "doctype",
                            "name": "Warranty Claim",
                            "label": _("Warranty Claim"),
                    },
                ]
            },
                        {
                    "label": _("Shop Floor"),
                    "icon": "icon-file",
                    "items": [
                    {
                            "type": "report",
                            "name": "Job Assignment",
                            "label": _("Job Assignment"),
                    },
                    {
                            "type": "report",
                            "name": "Stock Request",
                            "label": _("Stock Request"),
                    },   
                    {
                            "type": "report",
                            "name": "Job Quality Check",
                            "label": _("Job Quality Check"),
                    },   
                ]
            },
            {
                    "label": _("Billing"),
                    "icon": "icon-file",
                    "items": [
                    {
                            "type": "doctype",
                            "name": "Sales Invoice",
                            "label": _("Billing"),
                    },
                    {
                            "type": "doctype",
                            "name": "Insurance Authorization",
                            "label": _("Insurance Authorization"),
                    },
                    {
                            "type": "doctype",
                            "name": "Warranty Claim Approval",
                            "label": _("Warranty Claim Approval"),
                    },
                    {
                            "type": "doctype",
                            "name": "Release Clearance",
                            "label": _("Release Clearance"),
                    },
                    {
                            "type": "doctype",
                            "name": "Gate Pass",
                            "label": _("Gate Pass"),
                    },
                ]
            },
            {
                "label": _("Master Files"),
                "icon": "icon-file",
                "items": [
                    {
                        "type": "doctype",
                        "name": "Repair Operation",
                        "label": _("Repair Operations"),
                    },
                    {
                        "type": "doctype",
                        "name": "Part",
                        "label": _("Spareparts"),
                    },
                    {
                        "type": "doctype",
                        "name": "Techniciam",
                        "label": _("Technicians"),
                    },
                    {
                            "type": "doctype",
                            "name": "Insurance Company",
                            "label": _("Insurance Company"),
                    },
                    {
                            "type": "doctype",
                            "name": "Manufacturer",
                            "label": _("Manufacturer"),
                    },
                    {
                            "type": "doctype",
                            "name": "Subcontractor",
                            "label": _("Subcontractor"),
                    },
                ]
            },
            {
                "label": _("Settings"),
                "icon": "icon-file",
                "items": [
                    {
                        "type": "doctype",
                        "name": "Repair Settings",
                        "label": _("Repair Settings"),
                    },
                    {
                        "type": "doctype",
                        "name": "Workshop",
                        "label": _("Workshop"),
                    },
                    {
                        "type": "doctype",
                        "name": "Skill",
                        "label": _("Skills"),
                    },
                    {
                        "type": "doctype",
                        "name": "Skill Level",
                        "label": _("Skill Level"),
                    }
                ]
            }
		]
