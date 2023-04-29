
__version__ = '0.1.0'
# import frappe
# from frappe import _
# from frappe.website import render
# import gms

# def get_website_user():
#     from frappe.sessions import Session
#     return Session().get("user")

# def get_context(context):
#     website_user = get_website_user()
#     context.update({
#         "website_user": website_user
#     })

#     return context

# def get_response_html(path):
#     context = frappe._dict()
#     path = gms.public.my404page

#     try:
#         return render(path)
#     # except frappe.TemplateNotFoundError:
#     #     frappe.respond_as_web_page(_("404: Page not found"), _("Sorry we were unable to find the page you requested."), http_status_code=404)
#     except frappe.PermissionError:
#         frappe.local.flags.redirect_location = '/login'
#         raise frappe.Redirect

# frappe.website.get_response_html = get_response_html
