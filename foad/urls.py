# coding=utf-   8
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from foad.views import CodeCoursView


urlpatterns = patterns(
    '',
    url(r'^activate_cours/$', login_required(CodeCoursView.as_view()), name="activate_cours"),)

