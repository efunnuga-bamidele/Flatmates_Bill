import webbrowser

from pyfpdf import fpdf
import os

class PdfReport:
    """
    Create a pdf file that contains data about flatmates, their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_payment = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_payment = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = fpdf.FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add Icon
        pdf.image("images/home.png", w=30, h=30)

        # Add the font proparty
        pdf.set_font(family="Times", style="B", size=24)

        # Insert the Title
        pdf.cell(w=0, h=50, txt="Flatmates Bill", border=0, ln=1, align="C")
        # Insert the Period
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=80, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=13)
        pdf.cell(w=90, h=40, txt="Bill Amount", border=0)
        pdf.cell(w=80, h=40, txt=str(bill.amount), border=0)
        pdf.cell(w=80, h=40, txt=bill.unit, border=0, ln=1)

        # Insert Table Heading
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=80, h=40, txt="Name", border=0)
        pdf.cell(w=110, h=40, txt="Days Stayed", border=0)
        pdf.cell(w=110, h=40, txt="Amount", border=0)
        pdf.cell(w=110, h=40, txt="Unit", border=0, ln=1)

        # Insert dynamic data
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=80, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=110, h=20, txt=str(flatmate1.days_in_house), border=0)
        pdf.cell(w=110, h=20, txt=flatmate1_payment, border=0)
        pdf.cell(w=110, h=20, txt=bill.unit, border=0, ln=1)

        pdf.cell(w=80, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=110, h=20, txt=str(flatmate2.days_in_house), border=0)
        pdf.cell(w=110, h=20, txt=flatmate2_payment, border=0)
        pdf.cell(w=110, h=20, txt=bill.unit, border=0, ln=1)

        #Change directory
        os.chdir("pdf_reports")
        #Generate pdf report file
        pdf.output(self.filename)
        # self open pdf
        webbrowser.open(self.filename)