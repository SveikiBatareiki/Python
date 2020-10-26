# what is list after all?
# * ordered
# * collection of arbitrary objects (anything goes in)
# * nested (onion principle, Matrjoshka)
# * mutable - maināmas vērtības
# * dynamic - size can change

my_list = [5,6,"Valdis", True, 3.65] # most common way of creating list using [el1, el2]
print(my_list)
print(my_list[0])
my_list[1] = "Mr. 20" # lists can be mutated (unlike strings)
print("new list", my_list)
print(my_list[:3])
print(my_list[-2:])# last two
print(my_list[1:4], my_list[1:-1])
print(my_list[::2])# pa divi uz priekšu, no sākuma
print(my_list[1::2])# pa divi uz priekšu, no otrā
print("Valdis" in my_list) # true or false
print("al" in my_list) # this is false
needle = "al" # what we want to find in list
for item in my_list:
    print("Checking ", item)
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item}")

my_list.append("Bauskas alus") # append maina objektu, we modify list
my_list.append("Valmiermuižas alus") 
print("new list", my_list)

needle = "al" # what we want to find in list
find_list = [] # so we have an empty list in the beginning
for item in my_list:
    print("Checking ", item)
    if type(item) == str and needle in item: # type izmanto papildus drošībai, lai nepārbaudītu to ko nevajag, jo sarakstā ir arī int, in this case won't work without type, as there are aslo int
        print(f"Found {needle=} in {item}")
        find_list.append(item)
print(f"{needle=} found in {find_list}")
new_list = my_list + ["Kalējs", "Audējs"] # būs tas pats kas mmy list plus vēl divas vērtības
print("len for new_list", len(new_list), "len for my_list", len(my_list))

#how to convert all values to str
str_list = []
for item in my_list:
    str_list.append(str(item))# so if item is already string then nothing will change
print(str_list)

#list comprehensions make it even shorter
str_list_2 = [str(item) for item in my_list]
print(str_list_2)

print(str_list == str_list_2, str_list is str_list_2)# first checks if data are the same, second shows if objects are different

beer_list = [item for item in str_list if needle in item]# katrs items kas ir mūsu sarakstā, ja ir adata
print(beer_list)
#beer_list += "Užavas alus" šādi nedrīkst darīt
beer_list += ["Užavas alus"]
print(beer_list)
print(beer_list[-1])# prints last
last_beer = beer_list.pop() # also in place meaning I destryed the last value
print(last_beer, beer_list)
beer_list.append(last_beer)

print(beer_list.count("alus"))#only exact matches
print(beer_list)
#print(new_list.index("alus"))
beer_list.insert(2, "alus")# so it will insert before indec 2 (meaning 3rd element)
print(beer_list)
print("count alus", beer_list.count("alus"))
print("index alus", beer_list.index("alus"))
beer_list.remove("Užavas alus")
print(beer_list)
beer_list.reverse() # reversed list
print(f"reversed {beer_list}")
beer_list.sort()# modifies existing
print(f"sorted {beer_list}")
print(f"max = {max(beer_list)}, minimum = {min(beer_list)}")

total = 0
numbers = [1, 6, -8.16, 11, 3434]
print(numbers)
for n in numbers:
    total +=n
print(total)

sentence = "Quick brown fox jumped over a sleeping dog"
words = sentence.split()#default split is by whitespace
print(words)
words[2] = "Bear"
print(words)
new_sentence = " ".join(words) # we will losa any double or triple whitespaces
print(new_sentence)
funky_sentence = "*:*".join(words)
print(funky_sentence)

numbers = list(range(10))# we cast to list ou range object
print(numbers)
squares = []
for n in numbers:#could also use range(10)
    squares.append(n*n)
print(squares)
squares_2 = [n*n for n in range(10) if n % 2 == 0]
print(squares_2)

list_a = [1,2,10,20]
list_b = [2,3,10,15]
result = max(sum(list_a), sum(list_b))
print(result)

last = list_b.pop() # pop function removes last one (or the one value which is indexed) and returns it
print(last)
