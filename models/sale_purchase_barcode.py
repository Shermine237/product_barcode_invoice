from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_barcode = fields.Char(string="Barcode", related='product_id.barcode', store=False, readonly=True)


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_barcode = fields.Char(string="Barcode", related='product_id.barcode', store=False, readonly=True)
