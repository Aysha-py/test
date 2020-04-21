
request = int(input("How many candies do you want?"))
if request in range(1, 10):
    print('candy\n'*request)
    print(f"You requested for {request} number of candies")
else:
    print("we ran out of stock")
