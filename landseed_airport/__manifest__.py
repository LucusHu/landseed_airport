# -*- coding: utf-8 -*-
{
    'name': "林新醫院",  # Module title
    'summary': "Medical Notify",  # Module subtitle phrase
    'description': """
Landseed Airport
==============
Description medical notify.
    """,  # Supports reStructuredText(RST) format
    'author': "Lucas",
    'website': "",
    'category': 'Tools',
    'version': '14.0.2',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/medical_notify.xml',
    ],
    'application': True,
    'installable': True,
}
