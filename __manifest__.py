{
    "name": "Product Barcode on Documents",
    "version": "3.0",
    "author": "ABCD",
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
    "installable": True,
    "application": False,
}
