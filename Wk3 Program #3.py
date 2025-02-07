print("Thank you for using Fast Freight Shipping Company!")
weight = float(input("Enter you packages weight in pounds: "))

#find the price
if weight <= 2:
    charge = 1.5 * weight
elif weight > 2 and weight <= 6:
    charge = 3 * weight
elif weight > 6 and weight <= 10:
    charge = 4 * weight
else:
    charge = 4.75 * weight

print("Fast Freight Shipping Company will charge you $",charge)

