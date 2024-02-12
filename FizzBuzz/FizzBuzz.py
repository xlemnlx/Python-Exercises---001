try:
    userInput = int(input("Please enter a number:\n"))
except Exception as ex:
    print("Please enter a number only. \nException Type:", type(ex).__name__)
    exit()

if userInput % 3 == 0 and userInput % 5 == 0:
    print('"FizzBuzz"')
elif userInput % 5 == 0:
    print('"Buzz"')
elif userInput % 3 == 0:
    print('"Fizz"')
else:
    print('"' + str(userInput) + '"')
    #Concat doesn't add spaces when printing multiple objects.