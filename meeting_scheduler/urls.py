from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# from django.views.i18n import JavaScriptCatalog

app_name='meeting_scheduler'

urlpatterns = [
    path("offhour/create/<int:pk>", views.OffHourCreateView.as_view(), name="offhour_create"),
    # path("jsi18n", JavaScriptCatalog.as_view(), name="js-catalog"),
    path("appointment/create/<int:pk>", views.AppointmentCreateView.as_view(), name="appointment_create"),
    path("offhour/list", views.OffHourListView.as_view(), name="offhour_list"),
    path("schedule/list/", views.ScheduleListView.as_view(), name="schedule_list"),
    path("appointment/list/", views.AppointmentListView.as_view(), name="appointment_list"),
    path("appointment/accept/<int:pk>", views.appointment_approve, name="accept_appointment"),
    path("appointment/reject/<int:pk>", views.appointment_reject, name="reject_appointment"),
]