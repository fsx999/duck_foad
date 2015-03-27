# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import PermissionDenied
from mailrobot.models import Mail
from xworkflows.base import InvalidTransitionError
from duck_inscription.models import Wish
from foad.forms import AuditeurLibreForm
import xadmin
from foad.models import SettingsEtapeFoad, SettingsAnneeFoad, AuditeurLibreApogee
from xadmin import views

class SettingsEtapeFoadAdmin(object):
    exclude = ('cod_cur', 'cod_cyc')
    list_display = ('__str__', 'date_ouverture', 'date_fermeture', 'vu_etape_inf', 'c2i')
    list_editable = ('c2i',)


class SettingsAnneeFoadAdmin(object):
    exclude = ('cod_cur', 'cod_cyc')


xadmin.site.register(SettingsEtapeFoad, SettingsEtapeFoadAdmin)
xadmin.site.register(SettingsAnneeFoad, SettingsAnneeFoadAdmin)



class DossierAuditeurView(views.FormAdminView):
    form = AuditeurLibreForm
    title = 'Dossier Auditeur Inscription'

    def get_redirect_url(self):
        return self.get_admin_url('traitement_inscription_auditeur')

    def post(self, request, *args, **kwargs):
        self.instance_forms()
        self.setup_forms()

        if self.valid_forms():
            code_dossier = self.form_obj.cleaned_data['code_dossier']
            self.motif = "toto"
            choix = self.form_obj.cleaned_data['choix']
            try:
                wish = Wish.objects.get(code_dossier=code_dossier, is_auditeur=True)
                if wish.etape not in self.request.user.setting_user.etapes.all():
                    raise PermissionDenied
                elif choix == 'complet':
                    template = Mail.objects.get(name='email_auditeur_traite')
                    try:
                        wish.auditeur_traite()
                        self._envoi_email(wish, template)
                        AuditeurLibreApogee.objects.create_auditeur(wish.individu)
                        self.message_user('Dossier traité', 'success')
                    except InvalidTransitionError as e:
                        if wish.suivi_dossier.is_inscription_complet:
                            msg = 'Dossier déjà traité'

                            self.message_user(msg, 'warning')
                        elif wish.suivi_dossier.is_inactif:
                            wish.inscription_reception()
                            wish.inscription_complet()
                            self._envoi_email(wish, template)
                            self.message_user('Dossier traité', 'success')
                        else:
                            raise e
            except Wish.DoesNotExist:
                msg = 'Le dossier n\'existe pas'
                self.message_user(msg, 'error')
            except PermissionDenied:
                msg = 'Vous n\'avez pas la permission de traité ce dossier'
                self.message_user(msg, 'error')
            except InvalidTransitionError as e:
                self.message_user(e, 'error')
            except ValueError:
                self.message_user('Le code du dossier ne dois contenir que des chiffres', 'error')
        return self.get_response()

    def _envoi_email(self, wish, template):
        context = {'site': Site.objects.get(id=settings.SITE_ID_IED), 'wish': wish, 'motif': self.motif}
        email = wish.individu.user.email if not settings.DEBUG else 'paul.guichon@iedparis8.net'
        mail = template.make_message(context=context, recipients=[email])
        mail.send()

xadmin.site.register_view(r'^traitement_inscription_auditeur/$', DossierAuditeurView, 'traitement_inscription_auditeur')