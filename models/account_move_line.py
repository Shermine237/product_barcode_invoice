from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_barcode = fields.Char(
        string="Barcode",
        compute="_compute_product_barcode",
        store=False,
        readonly=True
    )

    @api.depends('product_id')
    def _compute_product_barcode(self):
        for line in self:
            line.product_barcode = line.product_id.barcode or ''
