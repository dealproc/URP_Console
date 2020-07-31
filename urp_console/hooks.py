# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "urp_console"
app_title = "Urp Console"
app_publisher = "asdf"
app_description = "asdf"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "asdf"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/urp_console/css/urp_console.css"
# app_include_js = "/assets/urp_console/js/urp_console.js"

# include js, css files in header of web template
# web_include_css = "/assets/urp_console/css/urp_console.css"
# web_include_js = "/assets/urp_console/js/urp_console.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "urp_console.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "urp_console.install.before_install"
# after_install = "urp_console.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "urp_console.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Customer": {
        "after_insert": "urp_console.urp_console.doctype.urp_customer.urp_customer.new_customer",
		"after_rename": "urp_console.urp_console.doctype.urp_customer.urp_customer.after_rename_user",
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"urp_console.tasks.all"
# 	],
# 	"daily": [
# 		"urp_console.tasks.daily"
# 	],
# 	"hourly": [
# 		"urp_console.tasks.hourly"
# 	],
# 	"weekly": [
# 		"urp_console.tasks.weekly"
# 	]
# 	"monthly": [
# 		"urp_console.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "urp_console.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "urp_console.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "urp_console.task.get_dashboard_data"
# }

