# 1. Uzdevums analizēt Veidenbauma dzeju
# Lejuplādejam texta failu no šejienes -> Save As
# https://raw.githubusercontent.com/ValRCS/Python_RTU_08_20/master/data/veidenbaums.txt
# Vai no šejienes:
# https://www.das.lv/platforma/pluginfile.php/3439/mod_resource/content/1/veidenbaums.txt
# Var arī vienkārši git pull visam repozitorijam: 
# https://github.com/ValRCS/Python_RTU_08_20
# 1a -> uzrakstam funkciju file_line_len(fpath), kas atgriež rindiņu skaitu failā
# pārbaudam file_line_len("veidenbaums.txt") -> vajadzētu būt 971
# iespējams jums veidenbaums.txt nebūs tajā pašā mapē, tad lietojam relatīvo ceļu uz failu
# 1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
# Tātad mums nederēs rindiņas bez teksta un nederēs dzejoļu virksraksti.
# PS vēlams izmantot encoding = "utf-8"a
# 1c -> uzrakstam funkciju save_lines(destpath, lines)
# Šī funkcija noglabās destpath faila ceļā(tātad fails vai fails ar ceļu), visas lines
# 1d -> izsaucam get_poem_lines uz veidenbaums.txt un tad rezultātu saglabājam veidenbaums_poems.txt (turpat kur ir jau veidenbaums) izmantojot save_lines funkciju
# 1e -> uzrakstam funkciju clean_punkts(srcpath,destpath)
# funkcija atvērs srcpath failu, attīrīs to no https://docs.python.org/3/library/string.html#string.punctuation
# un saglabās destpath 
# izsaucam uz veidenbaums_poems.txt un destpath būs veidenbaums_no_punkts.txt

# Droši vien nepietiks laika bet pamēģinam pa brīvdienām
# 1f -> uzrakstam funkciju get_word_usage(srcpath, destpath)
# funkcija atver failu un atrod biežāk lietotos vārdus
# ieteikums izmantot Counter moduli !
# uzskatīsim, ka vārdi tiek atdalīti vai nu ar whitespace vai newline (vecais labais split noderēs)

# populārāku vārdu sarakstu ar lietojuma biežumu saglabāam destpath
# Varam tagad pārbaudīt rezultātus gan uz veidenbaums_no_punkts.txt, gan uz veidenbaums_poems.txt

import os

#1a
def file_line_len(fpath):    
    with open(fpath, encoding="utf-8") as f:
    #     line_count = 0
    #     filtered_lines = [line.rstrip("\n") for line in f]
    #     for line in filtered_lines:
    #         line_count +=1
    #   return print(line_count)
    #   return print(sum([1 for lines in open(fpath)]))#Reiņa, bet jāpiečinī
        return len(f.readlines())
    
print(file_line_len("veidenbaums.txt"))

#1b
def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:
        poem_list = []
        filtered_lines = [line.rstrip("\n") for line in f]
        for line in filtered_lines:
            if line != "n"  and line !="" and line.endswith("***") == False :
                poem_list.append(line)
    return print(poem_list)

get_poem_lines("veidenbaums.txt")

#1c

def save_lines(destpath, lines):
    with open(destpath, "w" encoding=encoding) as f:
        for line in lines:
            f.write(lines)
#1d
save_lines("veidenbaums_poems.txt",get_poem_lines("veidenbaums.txt"))#doesn't work