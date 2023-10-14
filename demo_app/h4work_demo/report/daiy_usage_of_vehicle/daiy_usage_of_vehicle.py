# Copyright (c) 2023, H4work and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [
		{
			"label": "Vehicle",
			"fieldname": "days",
			"width": 400,
		},			
		{"label": "Hours", "fieldname": "hours", "fieldtype":"float", "width": 200},
	], []

	rec = frappe.get_all(
		"Service Vehice Travel", fields=["total_hours", "vehicle"], filters={"docstatus": 1}
	)

	hours_in_total = {}

	for hrec in rec:
		if hrec.days in hours_in_total:
			hours_in_total[hrec.days] = hours_in_total[hrec.days] + hrec.total_hours
		else:
			hours_in_total[hrec.days] = hrec.total_hours
		
	for days, hours in hours_in_total.items():
		data.append({"days": days, "hours": hours})

	chart = {
		"data": {
			"labels": ["Days", "Months"],
			"datasets": [
				{
					"name": "Daily Vehicle Usage", 
					"values": [180, 480]
				}
			]			
		},
		"type": "pie"
	} 	

	return columns, data, None, chart, None


