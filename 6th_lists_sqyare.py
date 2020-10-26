# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads 
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
# PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk

first = input("Please enter first number ")
last = input("Please enter last number ")

i = 0
number_list = []
square_list = []

for i in range(int(last) - int(first)+1):
    current = (int(first) + i) ** 3
    number_list.append(current)
    print(f"{current} cube is: {number_list[i]}")
    #i += 1 this is not needed, it will be done automatically in for cycle

print(f"All cube are: {number_list}")