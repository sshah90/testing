from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
urlpatterns=[
    url(r'^$', views.home, name="home"),
    url(r'^user/$', views.data_base, name="user"),
    url(r'^login/$',login,{'template_name':'login.html'},name="login"),
    url(r'^signup/$',views.signup,name="signup")





]