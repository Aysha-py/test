def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


output = fizz_buzz(13456)
print(output)
