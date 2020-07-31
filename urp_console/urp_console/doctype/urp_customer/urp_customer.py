# Copyright (c) 2020, asdf and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, cint, cstr, today
import random
import string

class URPCustomer(Document):

	def validate(self):
		pass

	def before_save(self):
		for tenant in self.tenants_ref:
			if not tenant.tenant_key:
				# Create a new key.
				tenant.tenant_key = get_random_alphanumeric_string(10)
				# TODO: publish new tenant_created event into EventStore
		pass

	def on_change(self):
		for tenant in self.tenants_ref:
			if tenant.is_locked:
				# publish tenant_locked
				pass
			else:
				# publish tenant_unlocked
				pass

			if tenant.is_closed:
				# publish tenant_closed
				pass
			else:
				# publish tenant_reopened
				pass

		pass

	def after_rename(self, olddn, newdn, merge=False):
		if frappe.defaults.get_global_default('cust_master_name') == 'Customer Name':
			frappe.db.set(self, "customer_name", newdn)

	def autoname(self):
		cust_master_name = frappe.defaults.get_global_default('cust_master_name')
		if cust_master_name == 'Customer Name':
			self.name = self.get_customer_name()
		else:
			set_name_by_naming_series(self)

	def get_customer_name(self):
		if frappe.db.get_value("URP Customer", self.customer_name):
			count = frappe.db.sql("""select ifnull(MAX(CAST(SUBSTRING_INDEX(name, ' ', -1) AS UNSIGNED)), 0) from `tabURP Customer`
				 where name like %s""", "%{0} - %".format(self.customer_name), as_list=1)[0][0]
			count = cint(count) + 1
			return "{0} - {1}".format(self.customer_name, cstr(count))

		return self.customer_name

# def get_random_alphanumeric_string(length):
def get_random_alphanumeric_string(length):
	letters_and_digits = string.ascii_letters + string.digits
	result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
	return result_str

def rename_customer(old, new, merge, _, __):
	frappe.rename_doc("URP Customer", old, new, merge)
	customer = frappe.get_doc("URP Customer", new)
	customer.name = new
	customer.save()
	# customer = frappe.get_doc("URP Customer", new)
	# customer.customer_name = new
	# customer.name = new
	# customer.save()
	pass

def new_customer(customer, method):
	urpcustomer = frappe.get_doc(doctype = "URP Customer", customer_name = customer.customer_name)
	urpcustomer.name = customer.name
	urpcustomer.insert()
	frappe.db.commit()
	pass