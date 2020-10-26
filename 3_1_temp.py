import sys

try:
    temperature: float = float(input("Please input your temparature"))
except ValueError as e:
    print("Incorrect value. Please enter number")
    sys.exit(1) # we exit early

if temperature > 35:
    if temperature <= 37:
        print("All good")
    else:
        print("Possible feaver")
else: 
    print("Isn't it too cold?")
