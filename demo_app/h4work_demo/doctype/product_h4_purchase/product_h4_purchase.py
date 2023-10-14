# Copyright (c) 2023, H4work and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ProductH4Purchase(Document):
	def before_save(self):
		products = self.products
		
		total_amount = 0
		change1 = 0
		for item in products:
			total_amount += item.price * item.quantity
		
		change1 = self.p_amount - total_amount
		self.total_amount = total_amount
		self.change = change1 