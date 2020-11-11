import os
print(os.getcwd())

with open("frost.txt") as f:#with mums garantē faila automatīsku aizvēršanu kad beidzās with atkāpe
    print(f.read())
    print("file is still open")
    print("Trying again")
    print(f.read())#no error, but where is content?
    #Kā Diana teica fails jau ir līdz galam nolašits, tā teikt lenta ir aizgājusi līdz galam, vai vēl tuvāk būtu vinilplate ir izspēlējusies līdz galam
    #Iemesls tam ir tas, ka ļoti reti mēs gribam vēlreiz failu lasīt, parasti tam ko vajag vajadzētu būt atmiņā un failiam ciet
    f.seek(0)#put's needle in the beginning of file
    print(f.read(20))
    print(f.read(10))
    # f is still open here
    f.seek(0)
    res = f.read()#not very efficiend could read everything in the beginning
# ../ nozīme kāpties vienu līmieni uz augšu
# "./12th_lesson/frost.txt" visio opens file from upper folder, in order to show in this can either write here, or write here in terminal cd 12th_lesson
with open("frost.txt", encoding="utf-8") as f:
    #filtered_lines = [line for line in f if "roads" in line]
    filtered_lines = [line.rstrip("\n") for line in f if line.startswith("And")]#possible to use regex from re

# f parasti izmanto faila lasīšanai, fin - ielasīšana, fout - ierakstīšanai (in/out)

with open("frost.txt", encoding="utf-8") as fin, open ("frost-yelling.txt", mode = "w", encoding="utf-8") as fout:
    for line in fin:#for each line in incoming file
        if line[0] == "n":
            fout.write("*"*40+"\n")
        else:
            fout.write(line.upper())#keeping also newlines

with open("frost-yelling.txt") as f:
    print(f.read())




