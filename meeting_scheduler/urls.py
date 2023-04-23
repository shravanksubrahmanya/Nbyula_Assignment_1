from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# from django.views.i18n import JavaScriptCatalog

app_name='meeting_scheduler'

urlpatterns = [
    path("offhour/<int:pk>", views.OffHourCreateView.as_view(), name="offhour_create"),
    # path("jsi18n", JavaScriptCatalog.as_view(), name="js-catalog"),
]