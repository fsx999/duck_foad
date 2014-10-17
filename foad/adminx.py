# coding=utf-8
from __future__ import unicode_literals
import xadmin
from foad.models import SettingsEtapeFoad, SettingsAnneeFoad


class SettingsEtapeFoadAdmin(object):
    exclude = ('cod_cur', 'cod_cyc')
    list_display = ('__str__', 'date_ouverture', 'date_fermeture', 'vu_etape_inf')


class SettingsAnneeFoadAdmin(object):
    exclude = ('cod_cur', 'cod_cyc')


xadmin.site.register(SettingsEtapeFoad, SettingsEtapeFoadAdmin)
xadmin.site.register(SettingsAnneeFoad, SettingsAnneeFoadAdmin)
