# Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)
#
# If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# If he doesn't get 10 hoops, return the string "Keep at it until you get it".

amountHoop = int(input('Enter how many times the hoop goes round: '))

output = 'Great, now move on to tricks' if amountHoop >= 10 else 'Keep at it until you get it'
print(output)
