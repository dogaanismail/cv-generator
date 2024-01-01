from django.contrib import admin
from django.urls import path
from CV_gen.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("cv_list", cv_list, name="list"),
    path("cv/<int:num>", cv_download, name="cv_down"),
    path('submit', submit)
]
