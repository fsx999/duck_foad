# coding=utf-8
from __future__ import unicode_literals
from admin_tools.dashboard import modules
from django.core.urlresolvers import reverse
from pal2.dash import DashBoardConfig


class Foad(DashBoardConfig):
    perms = ['auth.foad']

    def application(self, user, children):
        application = [{'title': u"Activation des cours ", 'url': reverse("activate_cours"), 'external': False}]
        children.append(modules.LinkList(u'FOAD', children=application))
