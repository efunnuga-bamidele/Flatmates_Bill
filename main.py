from flat import Bill, Flatmate
from reports import PdfReport

print("Hey user, Enter data for bill calculation!")
amount = float(input("Enter the bill amount: "))
currency = input("What is the currency type for the bill? E.g 'NGN': ")
period = input("What is the bill period? E.g 'January, 2020': ")
flatmate1_name = input("What is your name? ")
flatmate1_days_in_house = int(input(f"How many days did {flatmate1_name} stay in the house? "))
flatmate2_name = input("What is the name of the other flatmate? ")
flatmate2_days_in_house = int(input(f"How many days did {flatmate2_name} stay in the house? "))

the_bill = Bill(amount=amount, period=period, unit=currency)
flatmate_one = Flatmate(name= flatmate1_name, days_in_house=flatmate1_days_in_house)
flatmate_two = Flatmate(name= flatmate2_name, days_in_house=flatmate2_days_in_house)

print(f"{flatmate1_name} pays: ", round(flatmate_one.pays(bill=the_bill, call_flatmate=flatmate_two), 2), the_bill.unit)
print(f"{flatmate2_name} pays: ", round(flatmate_two.pays(bill=the_bill, call_flatmate=flatmate_one), 2), the_bill.unit)

pdf_report = PdfReport(filename=f"Flatmates bill for {the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate_one, flatmate2=flatmate_two, bill=the_bill)
