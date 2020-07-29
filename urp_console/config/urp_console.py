from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label": _("Users, Roles, and Permissions"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "URP Group",
              "label": _("Groups"),
              "description": _("People whohave enrolled for membership in the library."),
            },
            {
              "type": "doctype",
              "name": "URP Role",
              "label": _("Roles"),
              "description": _("System Roles"),
            },
            {
              "type": "doctype",
              "name": "URP Permission",
              "label": _("Permissions"),
              "description": _("Permissions per-application.  This should be based off an enumeration."),
            },
            {
              "type": "doctype",
              "name": "URP Application",
              "label": _("Applications"),
              "description": _("Hosted application services to be subscribed to."),
            }
          ]
      }
  ]
