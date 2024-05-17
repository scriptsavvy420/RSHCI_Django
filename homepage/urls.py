
from django.urls import re_path
from homepage import views

app_name = "homepage"

urlpatterns = [
    re_path(r'^$',views.homepage, name='homepage'),
    re_path(r'^terms/$', views.terms, name='Terms of Use'),
    re_path(r'^cookie/$',views.cookie, name='Cookie Policy'),
    re_path(r'^login/$',views.login, name='Login'),
    re_path(r'^login_wallet/$',views.login_wallet, name='login_wallet'),

    re_path(r'^wallet/$',views.wallet, name='Wallet'),
    re_path(r'^customadmin/$',views.admin, name='Custom Admin'),
    re_path(r'^wallet_manage/$',views.wallet_manage, name='Wallet Management'),
    re_path(r'^user_manage/$',views.user_manage, name='User Mnagement'),
    re_path(r'^send_mail/$', views.send_mail, name='send_mail'),
    re_path(r'^create_wallet/$', views.create_wallet, name='create_wallet'),


]