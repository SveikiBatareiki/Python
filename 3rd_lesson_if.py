a = int(input("Enter your value"))
print("You entered", a)
b = 9_000
if a>= 10:
    print("Do this when a is larger than 10")
    print(a, "value is bigger than 10")
    if a>100:
        print("a is more than 100")
    else:
        print("a is more than 10, but less than 100")
else:
    print("This will be visible when a is smaller than 10")
    print("lil a is",a)
    
print("This will be visible always")


    