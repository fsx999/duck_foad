# coding=utf-8
import floppyforms as forms
from duck_inscription.forms.adminx_forms import DossierReceptionForm


class CodeCoursPlateform(forms.Form):
    """
    prend le code du cours déjà créé
    """
    code = forms.CharField(label=u"Code cour")


class NewAuditeurForm(forms.Form):
    auditeur = forms.NullBooleanField(
        label=u"Voullez vous faire une demande de préinscription en tant qu'auditeur libre",
        widget=forms.Select(
            choices=(("", "-----"), ("True", "Oui"), ("False", "Non")),
            attrs={'class': 'required auto'}
        )
    )

    def clean_auditeur(self):
        if self.cleaned_data.get('auditeur', None) is None:
            raise forms.ValidationError(u'Vous devez choisir')
        return self.cleaned_data.get('auditeur', None)


class AuditeurLibreForm(DossierReceptionForm):
    choix = forms.ChoiceField(choices=(('complet', 'Complet'),),
                              widget=forms.RadioSelect(), required=True)
