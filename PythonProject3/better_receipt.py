"""
Prints borderline by repeating c 35 times on one line using forloop
"""
def print_line(c):

    for i in range(35):
        print(c, end="")

"""
prints header, border line with character c, store name, address line 1, address line 2, 
has opening and closing border lines
"""
def print_header(c, name, addr1, addr2):
    print_line(c)
    print()
    print(name)
    print(addr1)
    print(addr2)
    print_line(c)
    print()
    print()

"""
reads single line item data and prints out the product name, followed by the currency symbol 
and subtotal for that item, quantity/weight, unit price
"""
def process_item(curr):
    productname = input()
    price = float(input())
    quantity = float(input())
    total = price * quantity
    print(productname, curr, round(total,2))
    print("  ", quantity, "at", round(price, 2))
    return total

"""
loops through all the line items and uses a for-loop to call process_item(). 
It returns the overall total of all items (before tax)
"""
def process_cart(count, curr):
    total = 0.0
    for i in range(count):
        total += process_item(curr)

    return total

"""
prints footer, greeting message, and character c 35 times for border line
"""
def print_footer(c, greeting):
    print()
    print(greeting)
    print_line(c)
    print()

"""
main function, reads header info, greeting currency, c, currency, tax rate, 
item count using input function, prints header, 
does calculations and prints totals and tax, prints footer
"""
def main():
    c = input()
    name = input()
    addr1 = input()
    addr2 = input()
    greeting = input()
    curr = input()
    tax_rate = float(input())
    count = int(input())
    print_header(c, name, addr1, addr2)
    subtotal = process_cart(count, curr)
    tax = subtotal * (tax_rate/100)
    total = subtotal + tax
    print()
    print("SUBTOTAL:", curr, round(subtotal, 2))
    print("TAX (", tax_rate, "% ):", curr, round(tax, 2))
    print("TOTAL:", curr, round(total, 2))
    print_footer(c, greeting)

main()

"""
(.venv) rishikeshavadamarla@Rishis-MBP-8 PythonProject3 % python3 better_receipt.py < input1.txt 
-----------------------------------
Save Mart
7011 Gratiot Avenue
Detroit, MI 48207
-----------------------------------

Tillamook Greek Yogurt $ 7.02
   6.0 at 1.17
Honeycrisp Apples $ 5.39
   3.88 at 1.39
Best Food Mayonnaise $ 5.49
   1.0 at 5.49

SUBTOTAL: $ 17.9
TAX ( 6.0 % ): $ 1.07
TOTAL: $ 18.98

Shop Smart. Shop S Mart!
-----------------------------------
(.venv) rishikeshavadamarla@Rishis-MBP-8 PythonProject3 %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MBP-8 PythonProject3 % python3 better_receipt.py < input2.txt 
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
E.LECLERC Bayeux
Bd du 6 Juin,
14400 Bayeux, France
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Nous Cinq - Vin de France € 8.55
   1.0 at 8.55
Pierre Martinet Salade € 3.93
   3.0 at 1.31
Brioche Tressée Vendéenne € 3.45
   1.0 at 3.45
Tomate Cerise € 10.51
   2.11 at 4.98

SUBTOTAL: € 26.44
TAX ( 20.0 % ): € 5.29
TOTAL: € 31.73

Qui est le moin cher près de chez vous?
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
(.venv) rishikeshavadamarla@Rishis-MBP-8 PythonProject3 %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MBP-8 PythonProject3 % python3 better_receipt.py < input3.txt 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Sainsbury's Local
135-137 Bath Rd,
Cheltenham GL53 7LT, United Kingdom
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

Oat & Apple Crumble £ 4.65
   1.0 at 4.65
Free Range Eggs Large x6 £ 5.85
   3.0 at 1.95
Semi Skimmed Milk 2.27L £ 3.1
   2.0 at 1.55
Bramley Cooking Apples Loose £ 5.48
   2.49 at 2.2
Fresh Salad Cress 20g £ 0.4
   1.0 at 0.4
Baby Potatoes 1kg £ 1.2
   1.0 at 1.2

SUBTOTAL: £ 20.68
TAX ( 20.0 % ): £ 4.14
TOTAL: £ 24.81

Forgot the hot cross buns?
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
(.venv) rishikeshavadamarla@Rishis-MBP-8 PythonProject3 %
"""

