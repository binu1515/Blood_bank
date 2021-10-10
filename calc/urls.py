from django.conf.urls import include, url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


from . import views

# importing views from views..py

urlpatterns = [
	#path('add',views.add, name='add'),
	#path('admin/', admin.site.urls),
	path('',views.login,name='login'),
	path('home/',views.home,name='home'),
	path('display/',views.display, name = 'display'),
	path("register/",views.register,name = "register"),
	path("logout",views.logout, name="logout"),
    path('base/',views.base,name = 'base')
]
