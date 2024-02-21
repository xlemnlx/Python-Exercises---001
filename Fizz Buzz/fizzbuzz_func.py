def fizzbuzz(user_input):
    try:
        user_input = int(user_input)
        
        if user_input % 3 == 0 and user_input % 5 == 0:
            output = "FizzBuzz"
            return output
        elif user_input % 5 == 0:
            output = "Buzz"
            return output
        elif user_input % 3 == 0:
            output = "Fizz"
            return output
        else:
            output = str(user_input)
            return output
        
    except Exception as e:
        print(f"\nPlease enter a number only.\nError name: {type(e).__name__}")