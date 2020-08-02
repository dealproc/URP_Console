# URP_Console

This is an updated version of a credential manager I wrote about 7ish years ago (as of 2020).  It's on [GitHub](https://github.com/dealproc/CredentialManagement) and used NHibernate to do data storage and retrieval.  Instead of writing everything by-hand, I'm backboning this off of the [Frappe Framework](https://github.com/frappe/frappe) and [NEXTErp](https://github.com/frappe/erpnext).  Reading into the Frappe framework, a lot of the infrastructure heavy lifting for things like single-sign-on using an oauth credential is already built.  Something like [IdentityServer v4](https://github.com/IdentityServer/IdentityServer4) is a great option for building a single-sign-on solution, but the work involved in maintaining that system alone is counter-productive to building out the core systems that would be marketed.

The reason I am re-booting this is because of a curiosity mostly.  I want to see how python interacts and learn the language.  This is something that I've done before, so it's more a focus on the language and structure, and not as much of a focus on the business logic.

More to come... Just an initial brain-dump.
