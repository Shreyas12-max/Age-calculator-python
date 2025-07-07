# Age calculator
# created by : Shreyas
# created date : 6th July 2025

from datetime import date

print("Simple Age Calculator")

name = input("Enter ur name:")
birth_year = int(input("Enter ur birth year (YYYY): "))

current_year = date.today().year
age = current_year - birth_year

print("\nHi " + name + ", you r " + str(age) + "years old .")
