train = input ("Please choose a train enter the number coordinating with the destination: 1) New York City, NY 2) Buffalo, NY 3) Jersey City, NJ \n")

train = int(train)

cost = 0
if train == 1:
    cost = 3.25
elif train == 2:
    cost = 5.25
elif train == 3:
    cost = 7.50

print ("You have selected {} your cost is {} \nThere is a seat avalible on that train,\nPlease insert payment".format(train, cost))

print ("Thank you please take reciept below")
