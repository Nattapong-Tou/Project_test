from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import os
from tempfile import NamedTemporaryFile
# Create PDF File Invoice
# chose english as language
os.environ["INVOICE_LANG"] = "en"
# Detail Client
client = Client('Niracha')
client.address = '75/6 m.19 Thaitani 15 Klongnung Klongluang Phatumtani 12120'

# Detail Providor
providor = Provider('My Company', bank_account='2600420569', bank_code='2010')
providor.address = '75/6 m.19 Thaitani 15 Klongnung Klongluang Phatumtani 12120'
providor.zip_code = '12120'
providor.city = 'Bangkok'
providor.email = 'Nattapong.ng@tot.co.th'
providor.note = 'Test Create PDF with python'

creator = Creator('Nattapong')
# Example invoice.add_item(Item(จำนวน, ราคา, description='Item 1'))
invoice = Invoice(client, providor, creator)
invoice.currency_locale = 'en_US,UTF-8'
invoice.add_item(Item(1, 49000, description='Macbook Pro 2019'))
invoice.add_item(Item(60, 50, description='Item 2', tax=21))
invoice.add_item(Item(50, 60, description='Item 3', tax=0))
invoice.add_item(Item(5, 600, description='Item 4', tax=15))

pdf = SimpleInvoice(invoice)
pdf.gen('file/test_invoice.pdf', generate_qr_code=True)

