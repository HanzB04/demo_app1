# Copyright (c) 2023, H4work and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ServiceVehiceTravel(Document):
	def before_save(self):
		h_o_s = self.h_o_s

		total_hours = 0
		for item in h_o_s:
			total_hours += item.h_o_s

		self.total_hours = total_hours