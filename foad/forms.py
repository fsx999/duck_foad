# coding=utf-8
import floppyforms as forms


class CodeCoursPlateform(forms.Form):
    """
    prend le code du cours déjà créé
    """
    code = forms.CharField(label=u"Code cour")
