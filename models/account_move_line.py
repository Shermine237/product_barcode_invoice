from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_barcode = fields.Char(
        string="Barcode",
        related='product_id.barcode',
        readonly=True,
        store=False,
    )
