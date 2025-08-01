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


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_delivery_orders_and_lines_data(self):
        """ Override the main report data generation to inject the barcode. """
        data = super()._get_delivery_orders_and_lines_data()
        for order_data in data.get('orders', []):
            if 'aggregated_lines' in order_data:
                for product_id, line_vals in order_data['aggregated_lines'].items():
                    product = self.env['product.product'].browse(product_id)
                    line_vals['barcode'] = product.barcode or ''
        return data


# Also add barcode on stock.move (parent move), used in main operations list

class StockMove(models.Model):
    _inherit = 'stock.move'

    product_barcode = fields.Char(
        string="Barcode",
        related='product_id.barcode',
        readonly=True,
        store=False,
    )
