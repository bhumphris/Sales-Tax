amount = 1
total_amount = 0
tax_percentage = .06
def tax(total_amount):
    print("your subtotal is: " + str(total_amount) + "$")
    finalcost = total_amount * tax_percentage
    print("YOur tax is: " + str(finalcost))
    print("and your grand total is: " + str(finalcost + total_amount))
while amount > 0:
    print("enter the amount of your item, or press '0'\n")
    amount = raw_input()
    cost = float(amount)
    if amount == 0:
        tax(total_amount)
        break
    print("your total is: " + str(total_amount) + "$")



