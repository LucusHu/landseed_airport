# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MedicalNotify(models.Model):
    _name = 'medical.notify'
    # _inherit = 'res.partner'
    _description = 'Medical Notify'

    notify_date = fields.Char(string='通報時間')
    notify_division = fields.Char(string='通報單位')
    phone = fields.Char(string='電話')
