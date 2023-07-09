twoDigitNumber = input("Type a two digit number: ")
print("Addition: " + str(int(twoDigitNumber[0]) + int(twoDigitNumber[1])))
print("Subtraction: " + str(int(twoDigitNumber[0]) - int(twoDigitNumber[1])))
print("Multiplication: " + str(int(twoDigitNumber[0]) * int(twoDigitNumber[1])))
print("Division: " + str(int(twoDigitNumber[0]) / int(twoDigitNumber[1])))
print(str(int(twoDigitNumber[0])) +" to the power of " + str(int(twoDigitNumber[1])) + ": " + str(int(twoDigitNumber[0]) ** int(twoDigitNumber[1])))
print("Floor Division: " + str(int(twoDigitNumber[0]) // int(twoDigitNumber[1]))) # Normal division but rounds to 0-point
print("Round to 2-point: " + str(round(int(twoDigitNumber[0]) / int(twoDigitNumber[1]), 2))) # Rounds to two decimal points

# Remember BIDMAS - Brackets () -> Indices ** -> Division and Multiplication are Equal / * -> Addition and Subtraction are also equal + -
# In cases where operations are of equal priority it goes Left to Right