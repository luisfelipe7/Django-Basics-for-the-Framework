from django.conf.urls import url
from . import views

urlpatterns = [
    # This is when you use an String ^
    url(r'^$', views.course_list, name="courseList"),
    # \d -> Refers to one or more digits
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$',
        views.step_detail, name="stepDetail"),
    url(r'(?P<pk>\d+)/$', views.course_detail, name="courseDetail"),
]
