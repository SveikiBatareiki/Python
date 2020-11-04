# Vai ir pangramma?
# uzrakstīt funkciju is_pangram, kas atgriež True, kad mytext parametrs satur visus burtus kas padoti a alfabetā.
# Savadāk atgriežam False.
# pangramma - teikums,vārdu virkne, kas satur visus alfabeta burtus - https://en.wikipedia.org/wiki/Pangram
# Atstarpes ignorējam,un uzskatam ka lielais burts ir tikpat derīgs kā mazais, t.i. šeit A un a -> a

# def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
#     '''
#     '''
#     return None # here it should return True or False
# is_pangram("abcd foo") == False
# is_pangram("The quick brown fox jumps over the lazy dog") == True
# is_pangram("The five boxing wizards jump quickly") == True #ieverojam lielais T šeit

#Aleksandra risinājums
def is_pangram(mytext, a='aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'):
    my_bool_result = set(a) < set(mytext.lower())
    return my_bool_result
 
print(is_pangram('Muļķa hipiji turpat brīvi mēģina nogaršot celofāna žņaudzējčūsku'))
print(is_pangram('Mīļš čehu frants jūk — žņaudz pūķi cilpā, bēg vāģos'))
print(is_pangram('Teksts, kas nav pangramma.'))
# Pangrammas ņemtas šeit: http://www.jurjans.lv/lvpp/

import string
print(string.ascii_lowercase)
print(is_pangram("The quick brown fox jumps over the lazy dog", a=string.ascii_lowercase))
