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
		pass

	def before_save(self):
		# load list of tenants from db for this customer.

		for tenant in self.tenants_ref:
			if not tenant.tenant_key:
				# Create a new key.
				tenant.tenant_key = get_random_alphanumeric_string(10)
				# TODO: publish new tenant_created event into EventStore
			
		pass


	# def get_random_alphanumeric_string(length):

def get_random_alphanumeric_string(length):
	letters_and_digits = string.ascii_letters + string.digits
	result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
	return result_str