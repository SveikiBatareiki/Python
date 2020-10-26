# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.

user_input = 0
sequence = 0
total = 0
num_list = []
sorted_list = []

while True:
    user_input = input(str("Please enter number, if yoy want to exit type 'q' "))
    if user_input == "q":
        print("End of counting game")
        break
    sequence += 1
    total = 0
    num_list.append(float(user_input))
    print(f"num_list {num_list}")
    for i in range(sequence):
        total += num_list[i-1]
        #print(f"Total count is {total}")
    print(f"Average value of all inserted numbers is {round(total/sequence, 2)}")
    sorted_list = sorted(num_list, reverse = False)
    print(f"Top 3 are {sorted_list[-3:]}, bottom 3 are {sorted_list[:3]}")