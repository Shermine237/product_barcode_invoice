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
        Product = self.env['product.product']
        for vals in res.values():
            prod = vals.get('product_id')
            # prod may be a record, an ID, or None
            if isinstance(prod, int):
                prod = Product.browse(prod)
            vals['barcode'] = prod.barcode if getattr(prod, 'barcode', False) else ''
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
