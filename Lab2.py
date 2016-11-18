def checkSeatAvailability():
    print("Checking Availability")

def verifyPayment():
    print("Verifing Payment")

train = input("Please choose a train enter the number coordinating with the destination:\n"
               " 1) New York City, NY 2) Buffalo, NY 3) Jersey City, NJ \n")

train = int(train)

cost = 0
if train == 1:
    cost = 3.25
elif train == 2:
    cost = 5.25
elif train == 3:
    cost = 7.50
#system checks
checkSeatAvailability()

print("You have selected {} your cost is {} \nThere is a seat available on that train,\n"
       "Please insert payment".format(train, cost))

#system connects to card company to verify payment
verifyPayment()

#system prints receipt
print("Thank you please take receipt below")
