#prices
hot_dog_price = 3.50
chili_dog_price = 4.50
cheese_price = 0.50
peppers_price = 0.75
grilled_onions_price = 1.00
tax_percent = 0.07


#choosing hot dog type
hd_choice = input("Enter either chili dog or hot dog: ")

if hd_choice == "chili dog":
    subtotal = chili_dog_price
elif hd_choice == "hot dog":
    subtotal = hot_dog_price
else:
    print("Invalid choice of hot dog. Please enter either 'Hot Dog' or 'Chili Dog'.")
    exit()


#choosing topings
cheese = input("Would you like cheese? (yes or no): ")
if cheese == "yes":
    subtotal += cheese_price
peppers = input("Would you like peppers? (yes or no): ")
if peppers == "yes":
    subtotal += peppers_price
grilled_onion = input("Would you like grilled onions? (yes or no): ")
if grilled_onion == "yes":
    subtotal += grilled_onions_price

#tax and total
tax = subtotal * tax_percent
total = tax + subtotal

#final payment
print("Hot Dog Cost: $",subtotal)
print("Tax: $",tax)
print("Total Cost: $",total)
