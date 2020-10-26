print("String fun")
food = "kartupelis"
print(type(food))
print(food[0]) # why zero, historic reasons - starts with zero
food_len = len(food)
print("garums ir",food_len)
print(food[9])
print(food[len(food)-1])#not pythonic, avoid!
print(food[-1], food[-10])
print(food[:9015])
print(food[0:5],food[:5])#two ways, how to reflect first 5
print(food[5:10], food[5:0],food[-5:])# ar -5 izdrukā pēdējos 5
food = "Auzu putra ar avenēm"
# print(food[-320])#too much negative will give IndexError
# print(food[4000])#too much POSITIVE will give IndexError
print(food[0:20:2])#drukā katru otro
print(food[::-1])#reversing string
myText = "Alice told rabbit 'go down the hole' and then followed"
print(myText)
multiLineString = """ We can write whatewer even go to a
new line
    use a tab
    use single ' and " double
    also so o n
"""
print(multiLineString)
print("min", min(food), "max", max(food), "lenght", len(food))
#food[3] = "Z"# this will not work
newFood = food.replace('u', 'ū')#replacing one letter with another and assigning it to new parameter
print(newFood)
zeFood = food[:3] + 'ZZZE' + food[4:]
print(zeFood)
capFood = food.capitalize()
print("capitalize ->", food.capitalize())
print("upper ->", food.upper())
print("lower ->", food.lower())
print("title ->", food.title())
print("capitalize+replace ->", food.capitalize().replace("A", "L"))
print("This variable has", food.count('a'), "a letters")
print("This variable has index", food.index('a'), "for a letter")

for c in food:
    print(c)

city = " Ogre  "
clean_city = city.lstrip() #removes spaces from left
print(clean_city)
clean_city = city.strip() #removes spaces from left and right
print(clean_city)
clean_city = city.rstrip()#removes spaces from right
print(clean_city)
clean_city = city.split() #The split() method splits a string into a list. You can specify the separator, default separator is any whitespace. Note: When maxsplit is specified, the list will contain the specified number of elements plus one
print(clean_city)

my_text = "burkānmaize"
print(my_text[2:9:2])

my_text = "baltie krekli"
print(my_text.title())

my_text = "bezdelīga"
print(my_text[-4:])

my_text = "Alise runāja runāja runāja"
print(my_text.replace("runāja", "dziedāja",2))# two tells, that only first two needs to be replaced