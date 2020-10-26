# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30

def add_mult(numbers_list):
    print(numbers_list)
    numbers_list.sort()
    print(f"Counting smallest numbers {numbers_list[0]} and {numbers_list[1]} and multiplying by largest {numbers_list[2]} result is {(numbers_list[0]+numbers_list[1])*numbers_list[2]}")

add_mult([4,2,5])
add_mult([5,9,0])

def add_mult2(*args):
    my_list = sorted(args)
    return my_list[0]+my_list[1]*my_list[-1]
    
print("Two smalles counted, multiplied by biggest", add_mult2(6,3,78,2,7))

def add_mult3(arg_list):
    my_list = sorted(arg_list)
    return my_list[0]+my_list[1]*my_list[-1]
    
print("Two smalles counted, multiplied by biggest", add_mult3([6,3,78,2,7]))