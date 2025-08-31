{
    "name": "Product Barcode on Documents",
    "version": "18.0.0.1.1",
    "author": "Charlie Rostant YOSSA",
    "description": """
This module for Odoo 18 allows displaying product barcodes directly:
    - on invoice lines
    - on quotation / sales order lines
    - on RFQ / purchase order lines
    - on delivery slip lines

The barcode appears both in the form view and in the generated PDFs.
        """,
    "depends": ["account", "product", "sale", "purchase"],
    "data": [
        "views/account_move_form.xml",
        "views/report_invoice_barcode.xml",
        "views/sale_order_form.xml",
        "views/purchase_order_form.xml",
        "views/stock_picking_form.xml",
        "views/report_saleorder_barcode.xml",
        "views/report_purchaseorder_barcode.xml",
        "views/report_purchasequotation_barcode.xml",
        "views/report_stock_picking_barcode.xml",
    ],
    "license": "LGPL-3",
    "images": ["static/description/cover.png"],
    "support": "contact@charlieyossa.com",
    "installable": True,
    "application": False,
}
