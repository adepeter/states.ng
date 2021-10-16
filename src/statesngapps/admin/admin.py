from django.contrib import admin


class StatesNGAdminSite(admin.AdminSite):
    site_header = 'StatesNG admin'
    site_title = 'StatesNG admin'
    index_title = 'StatesNG administration'
    empty_value_display = 'Not yet set'
    enable_nav_sidebar = True
    final_catch_all_view = True


admin_site = StatesNGAdminSite(name='StatesNG Admin')
