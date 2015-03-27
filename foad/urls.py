# coding=utf-   8
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from foad.views import CodeCoursView, NewAuditeurView, AuditeurView, AuditeurPdfView


urlpatterns = patterns(
    '',
    url(r'^activate_cours/$', login_required(CodeCoursView.as_view()), name="activate_cours"),
    url(r'^auditeur_libre/$', login_required(NewAuditeurView.as_view()), name='new_auditeur'),
      url(r'^auditeur/(?P<pk>\d+)/$', login_required(AuditeurView.as_view()), name="auditeur"),
      url(r'do_pdf_auditeur/(?P<pk>\d+)/$', login_required(AuditeurPdfView.as_view()),
      name="do_pdf_auditeur"),
)

