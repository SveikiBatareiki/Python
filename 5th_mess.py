# Lietotājs ievada vārdu.
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# Valdis -> Sidlav, pamatigs juceklis vai ne V?

initial = input(str("Please enter your name"))
reverse = initial[::-1]
first = initial[0]
print(initial, "->",reverse.capitalize() + ", pamatīgs juceklis, vai ne", first.capitalize())