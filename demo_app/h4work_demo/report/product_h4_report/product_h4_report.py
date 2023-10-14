# Copyright (c) 2023, H4work and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [
		{
			"label": "Customer Name",
			"fieldname": "customer",
			"fieldtype": "Data",
			"width": 250,
		},
		{"label": "Total Income", "fieldname":"total_income1", "fieldtype":"currency", "width": 180},			
	], []

	rec = frappe.get_all(
		"Product H4 Purchase", fields=["total_amount", "c_name as customer"], filters={"docstatus": 1}
	)

	total_inc ={}

	for record in rec:
		if record.brand1 in total_inc:
			total_inc [record.brand1] = total_inc[record.brand1] + record.total_amount
		else:
			total_inc[record.brand1] = record.total_amount

	for brand1, total_income1 in total_inc.items():
		data.append({"customer":brand1, "total_income1": total_income1})

	return columns, data
