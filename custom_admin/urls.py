
from django.urls import re_path

from custom_admin.views.auth import *
from custom_admin.views.dashboard import *
from custom_admin.views.users import *



app_name = "custom_admin"

urlpatterns = [
    re_path(r'^login$', admin_login, name='admin_login'),
    re_path(r'^dashboard$', index, name='admin_dashboard'),
    re_path(r'^users/list$', user_list, name='admin_users_list'),
    re_path(r'^users/create$', user_create, name='admin_users_create'),
    re_path(r'^users/setprice$', setprice, name='admin_users_setprice'),

    re_path(r'^users/(?P<user_id>\w+)$',user_info,name = 'user_info'),







]