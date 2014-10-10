# coding=utf-8
# Create your views here.
from django.db.utils import OperationalError
from django.views.generic import FormView
from foad.utils import open_cour
from foad import forms


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
