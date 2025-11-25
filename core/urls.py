"""


this is the place for the all urls and links 



"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home)
]
