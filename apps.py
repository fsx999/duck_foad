# coding=utf-8
from django.apps import AppConfig


class DuckFoad(AppConfig):
    name = "foad"
    label = "foad"

    collapse_settings = [{
        "group_label": "Foad",
        "icon": 'fa-fw fa fa-circle-o',
        "entries": [{
            "label": 'Settings etape foads ',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/foad/settingsetapefoad/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Settings annee foads',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/foad/settingsanneefoad/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }, ]