#!/usr/bin/python3

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
cert = sys.path.append('/Users/agunb/OneDrive/Desktop/certificate')

def encrypt(input_file, password):
    pdf = pdfFileReader(input_file)
    writer = PdfFileWriter() # creating an empty PDF file
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        writer.addPage(page)

    writer.encrypt(password)

    with open('encrypted_' + input_file, 'wb') as output_file:
        writer.write(output_file)

encrypt(cert, 'password')
