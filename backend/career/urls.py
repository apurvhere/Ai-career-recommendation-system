from django.urls import path
from . import views
urlpatterns=[path("health/",views.health),path("careers/",views.careers),path("resume/parse/",views.parse_resume),path("recommend/",views.recommendations),path("skill-gap/",views.gaps),path("history/",views.history),path("history/<int:record_id>/",views.delete_history)]
