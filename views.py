# coding=utf-8
# Create your views here.
from django.conf import settings
from django.db.utils import OperationalError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView
from duck_inscription.models import Wish, SettingsEtape
from foad.forms import NewAuditeurForm
from foad.utils import open_cour
from foad import forms
from xhtml2pdf import pdf as pisapdf
from xhtml2pdf import pisa

class CodeCoursView(FormView):
    template_name = "foad/CodeCours.html"
    form_class = forms.CodeCoursPlateform

    def form_valid(self, form):
        code = form.cleaned_data['code']
        try:
            open_cour(code)
            message = u"Le cour est bien créé"
        except OperationalError:
            message = u"Le cour est déjà créé"
        return self.render_to_response(self.get_context_data(form=form, message=message))


class NewAuditeurView(FormView):
    form_class = NewAuditeurForm
    template_name = "duck_inscription/wish/auditeur_libre/new_auditeur.html"

    def form_valid(self, form):
        if form.cleaned_data['auditeur'] is True:
            individu = self.request.user.individu
            if Wish.objects.filter(is_auditeur=True).count() > 200:
                return redirect('home')
            wish = Wish.objects.get_or_create(
                individu=individu,
                etape=SettingsEtape.objects.get(cod_etp="L1NPSY"),
                is_reins=False,
                code_dossier=individu.code_opi,
                is_auditeur=True
            )[0]
            wish.auditeur()
            return redirect(wish.get_absolute_url())

        return redirect('accueil')

    def form_invalid(self, form):
        return super(NewAuditeurView, self).form_invalid(form)


class AuditeurView(TemplateView):
    template_name = "duck_inscription/wish/auditeur_libre/auditeur.html"

    def get_context_data(self, **kwargs):
        context = super(AuditeurView, self).get_context_data(**kwargs)
        context['wish'] = self.request.user.individu.wishes.get(pk=self.kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        if request.GET.get("valide", False):
            context['wish'].valide = True
            context['wish'].save()
        return self.render_to_response(context)




class AuditeurPdfView(TemplateView):
    template_name = "duck_inscription/wish/auditeur_libre/pdf_auditeur.html"
    templates = {
        'dossier_inscription': "duck_inscription/wish/auditeur_libre/pdf_auditeur.html",
        'formulaire_paiement_droit': "duck_inscription/wish/auditeur_libre/formulaire_paiement_frais.html",
        'etiquette': 'duck_inscription/wish/etiquette.html',
    }

    def get_context_data(self, **kwargs):
        context = super(AuditeurPdfView, self).get_context_data(**kwargs)
        context['student'] = context['individu'] = self.request.user.individu

        context['wish'] = context['voeu'] = self.request.user.individu.wishes.select_related().get(pk=self.kwargs['pk'])
        context['static'] = settings.BASE_DIR + '/duck_theme_ied/static/images/'

        return context

    def render_to_response(self, context, **response_kwargs):
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=auditeur_libre.pdf'
        pdf = pisapdf.pisaPDF()
        pdf.addDocument(pisa.CreatePDF(
            render_to_string(self.templates['etiquette'], context, context_instance=RequestContext(self.request))))
        pdf.addDocument(pisa.CreatePDF(render_to_string(self.templates['dossier_inscription'], context,
                                                        context_instance=RequestContext(self.request))))
        pdf.addDocument(pisa.CreatePDF(render_to_string(self.templates['formulaire_paiement_droit'], context,
                                                        context_instance=RequestContext(self.request))))
        pdf.join(response)
        return response
