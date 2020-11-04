# 3. Vārdnīcu tīrītājs
# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.
# !! Mainot vārdnīcas izmēru mēs nedrīkstam vienlaicīgi pa šo vārdnīcu staigāt(iterate)!
# aDivi varianti: vai nu staigājam pa kopiju my_dict.copy.items(), vai arī būvējam jaunu vārdnīcu

#3a
def clean_dict_value(d, bad_val) ->dict:# -> dict, šo python neņem vērā, bet dažādi pārbaudes rīki pārbauda, vai būs ievadīts īstais tips, laba lieta, bet prasa vairāk uzmanības un laiku
    new_dict = {}
    for key, value in d.items():
        if value != bad_val:
            new_dict[key] = value
    return new_dict
print(f"Clean_dict_value {clean_dict_value({'a':5,'b':6,'c':5}, 5)}")

#3b
def clean_dict_values(d: dict, bad_val_list: list) -> dict:# good thing is to give also types
    temp_dict = d.copy()
    for k in temp_dict:
        if d[k] in bad_val_list:
            deleted_value = d.pop(k)#deleted the key but returns value, here works the same as del
            print(f"We deleted {deleted_value}")    
    return d  
print(f"Clean_dict_values {clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5])}")

# shorter
def clean_dict_values2(d: dict, bad_val_list: list) -> dict:# good thing is to give also types 
    return {k:v for k,v in d.items() if d.get(k) not in bad_val_list}
print(f"Clean_dict_values2 {clean_dict_values2({'a':5,'b':6,'c':5}, [3,4,5])}")