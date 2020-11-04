# how to store and process data about garage
my_garage = ["paint can", "old papers", "rotting potatoes"]
my_garage_d = {"paints": ["white", "black"], "food": "potatoes"}

#empty class definition
class EmptyClass:
    pass

# i can create and based on class blueprint



class House:
    def __init__(self, color = "green", nails = 0):
        self.color = color
        self.nails = nails
        print(f"Initialized class instance with {self.color=} {self.nails=}")
    
    def simple_print(self):
        print(f"oh {self.color=} {self.nails=}")
        return self
    
    def set_color(self, new_color):
        #some validation
        self.color = new_color
        print(f"Changed color to {self.color}")

my_house = House()#creating new object, in other words class instance
#I've created object my_house based on house class blueprints
print(type(my_house))

friends_house = House(color="blue", nails = 1_000)
friends_house.simple_print()
print(my_house.color)
my_house.set_color("red")#good stile is to use classes for changing things, not to change them right away
my_house.simple_print()


class Garage:
    g_name = "just a garage" #better to use under def, not as seperate

    def __init__(self, color = "green", nails = 0):
        self.color = color
        self.nails = nails
        print(f"Garage initialized class instance with {self.color=} {self.nails=}")
    
    def simple_print(self):
        print(f"Garage oh {self.color=} {self.nails=} {self.g_name=}")
        return self
    
    def add_nails(self, new_nails = 1):
        self.nails += new_nails
        return self

    def set_nails (self, new_nail_count = 0):
        self.nails = new_nail_count
        return self
    
    #OOP getters method
    def get_current_nails(self):
        #formatting, data sanitaion, so no
        return self.nails+1000

    def __str__(self):#this is responsible for printing string
        return f"My garage {self.color} and name: {self.g_name}"
    
    def __repr__(self):
        return f"My garage {self.color} and name: {self.g_name}"

    def __add__(self, other):
        return self.nails + other.nails

    def __add__(self, other):
        new_color = self.color+"_"+other.color
        new_nails = self.nails + other.nails
        return Garage(new_color, new_nails)

#create new objects based on class definition
homer_garage = Garage(nails = 33)
flanders_garage = Garage(nails = 55)
#two different objects from the same blueprint(class definition)
print(id(homer_garage), id(flanders_garage))
print(homer_garage.g_name)
print(Garage.g_name)

milhouse_garage = Garage(color="purple")
milhouse_garage.simple_print()

homer_garage.g_name = "Homer's garage"
homer_garage.simple_print()
print(Garage.g_name)

print(homer_garage + flanders_garage)
super_garage = homer_garage + flanders_garage
print(super_garage)

class FancyGarage(Garage):#so we will use all things from old class also
    g_type = "Fancy"
    total_travel = 0

    def __init__(self, cars, wines, color = "gold"):
        super().__init__(color, nails = 2000)
        self.cars = cars
        self.wines = wines
        print("Fancy garage created")
        self.pretty_print()
    
    def pretty_print(self):
        print("This is pretty garage")

    def drive(self, distance):
        print(f"Driving {self.cars} a distance of {distance}")
        self.total_travel += distance
        return self #allows chaining of objects

    def get_longest_wine(self):
        wines_lenght = sorted(self.wines, key = len, reverse=True)
        return wines_lenght


burns_garage = FancyGarage("Bentley", ["Rioja", "Tempramillo", "Riesling"])
burns_garage.add_nails(10).drive(20).drive(5)
