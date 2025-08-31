# Product Barcode Module on Documents (Invoices, Quotations, RFQ, Orders, Delivery Slips)

This module for Odoo allows displaying product barcodes directly:

* on **invoice** lines
* on **quotation / sales order** lines
* on **RFQ / purchase order** lines
* on **delivery slip** lines

The barcode appears both in the form view and in the generated PDFs.

## Features

* **Barcode Column:** Adds a "Barcode" column in the list/form views of document lines (invoices, quotations, orders, RFQs/POs, delivery slips).
* **PDF Reports:** Integrates the "Barcode" column into the PDFs of invoices, quotations, purchase orders, and delivery slips.
* **Computed Field:** The barcode is dynamically retrieved from the product record associated with the document line.

## Installation

1. Copy the `product_barcode_invoice` folder into your Odoo addons directory.
2. Restart the Odoo service.
3. Go to the `Apps` menu (Applications).
4. Click on `Update Apps List`.
5. Search for the module **"Product Barcode on Documents"** and click on `Install`.

## Usage

Once the module is installed, the "Barcode" column will automatically appear on the mentioned documents, as well as in their PDF reports. No additional configuration is required.

## Compatibility

* Odoo 19.0, 18.0, 17.0, 16.0, 15.0

## Author

Charlie Rostant YOSSA (Shermine237)
