##This top section provides the first message and the wanted value of the chocolate bar

vPrice = float(16.90)
print("Your Chocolate Bar is $", vPrice, "HKD")
vCash = float(input("Please Enter Cash Payment"))
ChangeDue = round(vCash-vPrice,2)

##This sets the first reaction for the input cash for the chocolate bar that is wanted

if ChangeDue == 0:
    print("Thank you for purchasing!")
while vCash >= vPrice:
    print("We owe you change!")
    if ChangeDue - vCash:
        print("Here is $",ChangeDue)
        break
while vCash <= vPrice:
        print("You owe more money")
        break

##This explains how to determine the change given in specific coin values

while ChangeDue > 0:
   if ChangeDue >= 10:
        print("Putting $10 through the coin return slot")
        ChangeDue = ChangeDue - 10

   elif ChangeDue >= 5:
       print ("Putting $5 through the coin return slot")
       ChangeDue = ChangeDue - 5

   elif ChangeDue >= 2:
        print("Putting $2 through the coin return slot")
        ChangeDue = ChangeDue -2

   elif ChangeDue >= 1:
        print("Putting $1 through the coin return slot")
        ChangeDue = ChangeDue - 1

   elif ChangeDue >= 0.5:
        print ("Putting $0.5 through the coin return slot")
        ChangeDue = ChangeDue - 0.5

   elif ChangeDue <= 1:
        print ("Putting $0.1 through the coin return slot")
        ChangeDue = ChangeDue - 0.1

##This is a print summary of the Transactions that took place in the machine

print()
print("Summary of Chocolate Bar Transaction:")
print("Price of the Chocolate Bar:", vPrice)
print("Cash Paid by Customer:", vCash)
print("Change Due:", round(ChangeDue,2))
print("Total Change Given:",round(vCash-vPrice,2))
