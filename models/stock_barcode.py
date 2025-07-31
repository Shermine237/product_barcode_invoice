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

    def _get_aggregated_product_quantities(self, **kwargs):
        """Override to include barcode in aggregated dict for reports."""
        res = super()._get_aggregated_product_quantities(**kwargs)
        for vals in res.values():
            product = vals.get('product_id')
            vals['barcode'] = product.barcode if product else ''
        return res


# Also add barcode on stock.move (parent move), used in main operations list

class StockMove(models.Model):
    _inherit = 'stock.move'

    product_barcode = fields.Char(
        string="Barcode",
        related='product_id.barcode',
        readonly=True,
        store=False,
    )
