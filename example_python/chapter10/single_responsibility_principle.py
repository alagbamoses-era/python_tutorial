#!/usr/bin/python3



class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount * 1.18 # tax


class InvoicePrinter:
    def print_invoice(self):
        print(f"Total: {invoice.calculate_total()}")

invoice = Invoice(200)

printer = InvoicePrinter()
printer.print_invoice()

