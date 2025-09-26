# reading first, second, and third product
product1_name = str(input("First product: "))
price1 = float(input("Price: "))
quantity1 = int(input("Quantity: "))
product2_name = str(input("Second product: "))
price2 = float(input("Price: "))
quantity2 = int(input("Quantity: "))
product3_name = str(input("Third product: "))
price3 = float(input("Price: "))
quantity3 = int(input("Quantity: "))

# prints store header
print()
print("------------------------------")
print("S Mart")
print("123 Main Street")
print("Anytown, CA 12345")
print()

# computing line item totals and final subtotal
total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3
subtotal = total1 + total2 + total3

# print three line items
print(product1_name, round(total1, 2))
print("  ",quantity1, "at",  price1)
print(product2_name, round(total2, 2))
print("  ",quantity2, "at",  price2)
print(product3_name, round(total3, 2))
print("  ",quantity3, "at",  price3)
print()

# calculates clubcard savings and tax
clubcard_savings = 0.05 * subtotal
tax = 0.0913 * (subtotal - clubcard_savings)

# print receipt section with subtotal, clubcard savings, tax, grand total, and thank you farewell message
print("SUBTOTAL:",  round(subtotal, 2))
print("CLUBCARD Saving (5%):", round(clubcard_savings, 2))
print("TAX (9.13%):", round(tax, 2))
print("GRAND TOTAL:", round((subtotal - clubcard_savings + tax), 2))
print()
print("Thank you! Come again!")
print("Shop Smart, Shop S Mart!")
print("------------------------------")

"""
(.venv) rishikeshavadamarla@Rishis-MBP-8 Market Receipt Python Project % python3 Market\\ Receipt.py <input-good1.txt
First product: Price: Quantity: Second product: Price: Quantity: Third product: Price: Quantity: 
------------------------------
S Mart
123 Main Street
Anytown, CA 12345

Honey Crisp Apples 2.6
   2 at 1.3
Captain Crunch 6.6
   2 at 3.3
Wonder Bread 4.5
   3 at 1.5

SUBTOTAL: 13.7
CLUBCARD Saving (5%): 0.69
TAX (9.13%): 1.19
GRAND TOTAL: 14.2

Thank you! Come again!
Shop Smart, Shop S Mart!
------------------------------
(.venv) rishikeshavadamarla@Rishis-MBP-8 Market Receipt Python Project %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MBP-8 Market Receipt Python Project % python3 Market\\ Receipt.py <input-good2.txt 
First product: Price: Quantity: Second product: Price: Quantity: Third product: Price: Quantity: 
------------------------------
S Mart
123 Main Street
Anytown, CA 12345

Tillamook Greek Yogurt 6.0
   6 at 1.0
Heinz BBQ Sauce 4.4
   2 at 2.2
Best Food Mayonaise 3.99
   1 at 3.99

SUBTOTAL: 14.39
CLUBCARD Saving (5%): 0.72
TAX (9.13%): 1.25
GRAND TOTAL: 14.92

Thank you! Come again!
Shop Smart, Shop S Mart!
------------------------------
(.venv) rishikeshavadamarla@Rishis-MBP-8 Market Receipt Python Project %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MBP-8 Market Receipt Python Project % python3 Market\\ Receipt.py <input-good3.txt
First product: Price: Quantity: Second product: Price: Quantity: Third product: Price: Quantity: 
------------------------------
S Mart
123 Main Street
Anytown, CA 12345

CHAMPIGNON GEANT 3.27
   3 at 1.09
RISOTTO AU FROMAGE 13.34
   2 at 6.67
CHATAIGNES 7.2
   6 at 1.2

SUBTOTAL: 23.81
CLUBCARD Saving (5%): 1.19
TAX (9.13%): 2.07
GRAND TOTAL: 24.68

Thank you! Come again!
Shop Smart, Shop S Mart!
------------------------------
(.venv) rishikeshavadamarla@Rishis-MBP-8 Market Receipt Python Project %
"""
