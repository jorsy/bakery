# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero


class BakeryCategory(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "bakery_shop.category"
    _description = "Bakery Product Categories"
    _order = "id desc"

    # Basic
    name = fields.Char("CategoryName", required=True)
    description = fields.Selection(
        selection=[
            ("B", "Bread"),
            ("C", "Cakes"),
            ("K", "Koffiekoeken"),
            ("P", "Pastries"),
        ],
        string="Category Description",
    )
    active = fields.Boolean("Active", default=True)
