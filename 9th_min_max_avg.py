# 1. Min, Avg, Max
# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
# 1b tiem, kas pieredzējušāki
# Uzrakstiet funkciju get_min_med_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, medianu un lielāko vērtību no virknes.
# Median vērtība ir vērtiba, kas sakartotā virknē ir paša vidū. Ja virknes skaits ir pāra tad vidū ir divas vērtības.
# No vidus vērtībām tad ņem vidējo.
# get_min_med_max([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max("baaac") -> ('a','a','c')
#  # ar string var būt interesanti rezultāti pie pāra skaita ņemot vidējo, tāpēc labak dot abus vidējos
# get_min_med_max("faaacb") -> ('a', 'ab', 'f') 
# ienākošā sequence var būt tuple vai list ar vienāda tipa vērtībām, vai pat string.

#1a
def get_min_avg_max(sequence):
    total = 0
    for n in range(len(sequence)):
        total += sequence[n]
    return min(sequence), int(total/(n+1)), max(sequence)

print(get_min_avg_max([0,10.5,1,9]))

#1b
def get_min_med_max(sequence):
    sequence = sorted(sequence)
    middle = len(sequence)/2-1
    if middle%2 == 0:
        middle += 0.5
        middle = int(middle)
        if type(sequence) == int or type(sequence) == float:
            middle_item = (sequence[middle] + sequence[middle+1])/2
        else:
            middle_item = sequence[middle] + sequence[middle+1]
    else:
        middle += 0.5
        middle = int(middle)
        middle_item = sequence[middle]
    return min(sequence), middle_item, max(sequence)

print(get_min_med_max([1,5,8,4,3]))
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("baaaac"))