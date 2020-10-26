#FizzBuzz
for n in range (1,101):
    endsymbol = "\n"
    if n%5 ==0 and n%7 == 0:
        print("FizzBuzz", end=",")     
    elif n%5 == 0:
        print("Fizz", end=",")
    elif n%7 == 0:
        print("Buzz", end=",")
    else:
        print(n, end=",")
print("")
#Christmastree
height = int(input("Please input Christmastree height"))
i = 1
while i < height+1:
    print(" "*(height-i),"*"*(i*2-1))
    i += 1

#Prime number
number = int(input("Please input number"))
if number == 2:
    print("This IS a prime number")
else:    
    for i in range (1,round(number**0.5)):
        i += 1
        if number%i == 0:
            print("This is NOT a prime number")
            break
        elif i == round(number**0.5):
            print("This IS a prime number")      
