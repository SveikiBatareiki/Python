# 1. Reizinājumu summa
# Izmantojot standarta bibliotekas math sadaļu,
# Atrodiet funkciju kura sarēķina kādas virknes visu elementu reizinājumu (product)
# Importējiet uz izsauciet to pa tiešo.
# 1.b Uzrakstiet savu funkciju sum_prod(seq_a, seq_b) kas
# atgriež divu virknju reizinājumu summu
# sum_prod([2,3],[5,10,2]) == 106
# bonuss: uzrakstiet funkciju, kas atgriež neierobežota skaita virknju reizinājumu summu, t.i. katra virkne tiek sareizināta savā starpa un tad rezultāts sasummēts
# 1.c uzrakstiet savu moduli m_utils.py kurā ievietojiet savu jauno funkciju
# Atcerieties ielikt __main__  guard savā modulī!
# PS Importējiet vajadzīgo standarda biblioteku pašā moduļa sākumā
# 1.d izveidojiet main.py kurš importē m_utils un izsauc sum_prod
# 1.e ieliekiet m_utils.py sevis izveidotā mpak mapē un no main.py izsauciet sum_prod (iespējamie vairāki piegājieni)

#1a
import math
my_list = [2,3,4,6,7,2,6,3]
product = math.prod(my_list)
print(product)

#1b
def sum_prod(seq_a, seq_b):
    result = math.prod(seq_a)+math.prod(seq_b)
    return result

print(sum_prod([2,3],[5,10,2]))

#1b bonuss
def sum_prod_bon(*seq):
    result = 0
    for i in range (len(seq)):
        result += math.prod(seq[i])
    return result

print(sum_prod_bon([2,3],[5,10,2],[3,7,4,7]))