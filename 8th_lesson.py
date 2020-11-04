empty_dict = {}
print(len(empty_dict))
print(type(empty_dict))
tel = {"valdis": 2640, "līga": 2911}
print(tel)
tel["maija"] = 2653
print(tel)
print(tel["valdis"])# this lookup will be very fast 0(1) even with huge dictionary
key = "maija"
print(tel[key])
may_phone = tel[key]
print(may_phone)
# keys are unique, values can match for different keys
tel["pēteris"] = 2911
print(tel)
print(tel.keys(), type(tel.keys()))
key_list = list(tel.keys())# so I can create a list of dictionary keys
print(key_list)
value_list = list(tel.values())
print(value_list)
print("valdis" in tel)# so I can check for key in my dictionary
print("joker" in tel)
#print(tel["badkey"])
print(2640 in tel.values())# just keep in mind that this will be slow on big dictionaries - to search for key in values
my_key = "pēteris"
if my_key in tel:
    print(tel[my_key])
else:
    print("Couldn't find this key")
print(tel.get("valdis"))# this is faster
print(tel.get("nevaldis"))# deault is none if not found
print(tel.get("nevaldis", "Couldn't find this key"))# this is the same as before described if/else

# iterate over all items (key -> value pairs) in dictionary
for key, value in tel.items():
    #it is important not to modify this dictionary while we are looping overs it - it can brake loop
    print(f"{key=}, {value=}")
    #do more stuff with each key value pair


tel.setdefault("rūta", 2911)#idea to set key value pairs UNLESS it is already set
tel["valdis"] = 2911 #so changing value, if there is existing, then valdis phone number will be overwritten, if it won't exist, then new will be created

#searching based on phone number all pairs
value_to_find = 2911
new_dictionary =  {}
for key, value in tel.items():
    if value == value_to_find:
        new_dictionary[key] = value

print(new_dictionary)

del tel["pēteris"] #deleting key 
print(tel)

#tel.clear() #deleting all dictionary
print(tel)

#Dictionaty comprehension
plain_squares = {n: n*n for n in range(5)}# dictionary comprehension, if there is no str, then it is very similar to list, and could be mixed
print(plain_squares)
my_squares = {str(n): n*n for n in range(5)}# dictionary comprehension
print(my_squares)

squares = {}
for n in range(5):
    squares[str(n)] = n*n
print(squares)

print(squares == my_squares)# so dictionaries have same keys with same values
print(squares is my_squares)# but they are different objects this should be false

my_cubes = {f"Cube of {n}:": n**2 for n in range(8)}
print(my_cubes)
food = "kartupelis"
abc = "abcdefghij"
cypher = {k: v for k, v in zip(food, abc)}#merging food and abc - food is as key
print(cypher)
abc_dict = {v: i for i, v in enumerate(abc, start=1)}
print(abc_dict)
import string
all_letter_dictionary = {v: i for i, v in enumerate(string.ascii_uppercase, start=1)}
print(all_letter_dictionary)
zero_dict = {c: 0 for c in food} # katram pieliek nulli
print(zero_dict)

#Passing variable number of named arguments to function

def name_adder(**kwargs):#infinite number - **
    for key, value in kwargs.items():
        print(key,value)

def adder(*args):
    for arg in args:
        print(arg)

adder(1,5,6)

name_adder(first="Valdis", likes = "coding", loves = "potatoes")

def get_me_everything(*args, **kwargs):#order is important positional comes first!
    for key, value in kwargs.items():
        print(key,value)
    for arg in args:
        print(arg)

def get_me_all(a,b,*args, **kwargs):#order is important positional comes first! If star is removed, then it becomes mandatory
    for key, value in kwargs.items():
        print(key,value)
    for arg in args:
        print(arg)
    print(a,b)

get_me_all(10, "Homer", 5,20, greet = "Jello", boss = "Mr. Burns")
get_me_all("Doh", "Marge")

def filter_dictionary(in_dict, value_to_find=2911):#default values can be defined
    out_dictionary = {k:v for k,v in in_dict.items() if v == value_to_find} #k - key, v - value
    return out_dictionary

my_filtered_dictionary = filter_dictionary(tel)#default value is used
print(my_filtered_dictionary)

new_dictionary = filter_dictionary(tel, 2640)#searched value is defined
print(new_dictionary)

food = "kartupelis"
d = {c:c.upper()*2 for c in food}
print(d['c'])
