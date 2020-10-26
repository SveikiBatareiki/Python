salary = float(input("Please enter your salary"))
years = int(input("How many years have you worked here?"))

if years <2:
    print("Bonus is calculated if you have worked in company for more than 2 years")
else:
    print("You're bonus will be", round((years-2)*salary*0.15,2),"EUR")