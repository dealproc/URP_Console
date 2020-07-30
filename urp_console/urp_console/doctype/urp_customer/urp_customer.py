# -*- coding: utf-8 -*-
# Copyright (c) 2020, asdf and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import random
import string

class URPCustomer(Document):

	def validate(self):
		#frappe.throw(str(len(self.licenses_ref)))

		for tenant in self.tenants_ref:
			if not tenant.tenant_key:
				tenant.tenant_key = get_random_alphanumeric_string(10)

	def on_update(self):
		# licenses_ref
		pass


	# def get_random_alphanumeric_string(length):

def get_random_alphanumeric_string(length):
	letters_and_digits = string.ascii_letters + string.digits
	result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
	return result_str