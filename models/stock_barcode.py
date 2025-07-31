# -*- coding: utf-8 -*-
from odoo import models, fields


class StockMoveLine(models.Model):
    """Adds barcode on stock move line"""
    _inherit = 'stock.move.line'

    product_barcode = fields.Char(
        string="Barcode",
        related='product_id.barcode',
        readonly=True,
        store=False,
    )
