from django.test import TestCase
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font('Arial', '', 16)
pdf.cell(40, 10, 'hello', ln=1, border=True)
pdf.cell(80, 10, 'hello')
pdf.output('teste.pdf')