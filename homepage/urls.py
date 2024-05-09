
from django.urls import re_path
from homepage import views

app_name = "homepage"

urlpatterns = [
    re_path(r'^$',views.homepage, name='homepage'),
    re_path(r'^terms/$', views.terms, name='Terms of Use'),
    re_path(r'^cookie/$',views.cookie, name='Cookie Policy'),
    re_path(r'^send_mail/$', views.send_mail, name='send_mail'),
]