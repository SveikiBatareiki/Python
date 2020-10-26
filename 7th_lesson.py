# defining function
def go_eat():
    print("Go eat")
    print("Let's order food")

#calling function
go_eat()
go_eat()

#requirement that order_food is given an argument
def order_food(dish):
    dish = str(dish)
    print(f"I'm ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasy")
    # so dish stops working here
# no dish here

order_food("potatoes")
order_food("ice cream")
order_food(555)

#print(dish) this won't work because this doesn't exist here - outside function

def eat(food_list):
    print("Hello")
    for food_item in food_list:
        order_food(food_item)
        order_food("ice cream")
    print("Let's eat")
    print("Let's leave and be happy")

eat(["soup", "potatoes", "ice cream"])

def mult(a, b):
    print(f"Look, I'm multiplying {a} with {b} result is {a*b}")
    return a*b#with this it is possible also to print result afterwards, when function is called

mult(5,10)
print(mult(7,20))
mult("Beer", 3)
result = mult(10,50)
print(result)

def add(a=50, b=10):# this means that a and b are defined if user doesn't give other values
    inner_result = a+b

result = add(5,6)
print(result)

print(add(100))#this means that a = 100, but b is still 10
print(add())#this means that a is still a = 100, but b is still 10
print("Done adding")

#print(mult(add(3,5), add(2,1)))

def greeter(first, last, is_upper=False, add_suffix=""):#mandatory parameters are those, which are not definede already in function
    """
    Prints greeting
    Options - 
        is_upper - whether to capitalize
        add_suffix - what suffix to add
    """
    if is_upper:
        print(f"Hello {first.upper()} {last.upper()} {add_suffix}")
    else:
        print(f"Hello {first} {last} {add_suffix}")

greeter("Māra", "Kārkliņa")
greeter("Jānis", "Bērziņš", is_upper=True)
greeter("Diāna", "Siliņa", add_suffix="sveicam kursā!")
greeter("Viktor", " ", True)#is_upper is not necessary, but nice to include for clarity

print(min(1,2,-6,6,20,30))

def adder(*args): # so a list of arguments of any lenght
    print(f"My adder with {len(args)} arguments")
    for arg in args:
        print(arg)

adder(5,2, "Valdis")

def  mult(*args, multiplier=1):
    result = multiplier
    for arg in args:
        #could add an if here to check data type if we are not sure of nombers
        result *=arg
    return result

print(mult(2,10,5))
print(mult(2,10,5,-3.6))
print(mult(2,10,5,-3.6, multiplier=1000))
print(mult(2,10,5,-3.6, multiplier=0))
