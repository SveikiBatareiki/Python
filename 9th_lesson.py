my_tuple = ("Valdis", "programmer",34,200,[1,6,5],3, 4, {"drink":"milk", "animal":"cow"})
print(my_tuple)
print(my_tuple.count("programmer"))
print(my_tuple.index(3))#parāda trījnieka lokāciju

a = 10
b = 20
temp = a
a = b
b = a

#in python you can do this more easy
a, b = b, a# we can change even more a,b,c,d = d,c,b,a
print(a,b)
(name, job, age, top_speed, favourite_list, _ , _ , favourite_dict) = my_tuple# tuple unpacking
print(name, job, age, top_speed, favourite_list)
(name, job, _, top_speed, _) = my_tuple[:5]
print(name, _)

def getMinMax(my_num_list):
    return min(my_num_list), max(my_num_list)

print(getMinMax([1,6,4,7,2,8,99]))

my_tuple[-1]["car"] = ["vw"]# adds new as last one
print(my_tuple)

chars = set("abracadabra")#you pass an iterable to set(iterablehere)
print(chars)
len(chars)
print("a" in chars)# set membership check will be faster than in lists and tuples
print("e" in chars)

new_set = {"kartupelis"}
print(new_set)
food_item_set = set(["kartupelis"])
print(food_item_set)
chars = set("kartupelis")
print(chars)
print(new_set==food_item_set)
words = ["potato", "potatoes", "tomato", "Valdis", "potato"]
unique_words = set(words)
print(unique_words)

numbers = set(range(12))
print(numbers)
n3_7 = set(range(3,8))
print(n3_7)
print(n3_7.issubset(numbers))
print(n3_7<= numbers) # let's you have equal sets
print(n3_7 < numbers)# this will be false if both sets are equal
n5_9 = set(range(5,10))
print(n5_9)
print(n3_7|n5_9)

print(sorted(tuple(set("alus") - set("akas"))))

my_tuple = ([1,2,3],"Python",["coding", "rocks"])
print(my_tuple[-1][0][-1])#gives only "g"

my_tuple = tuple(range(5))
a,b,c,d,e = my_tuple
print(my_tuple.index(d))

result = set([1,2,3]) | set([2,3,4,5]) #combines unique
print(result)

result = set([1,2,3]) & set([2,3,4,5])# shows unique
print(result)