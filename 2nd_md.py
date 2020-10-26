print("Pirmais uzdevums")
name = input("Sveiki, ka Tevi sauc?")
print(name, "cik jums gadu?")
years = input()
print("Jums bus 100 gadi pec", 100-int(years))
import datetime # par importiem runāsim atsevišķi
currentYear = datetime.datetime.now().year
print("Tas bûs", currentYear + 100-int(years))


print()
print("Otrais uzdevums")
platums = input("Kads ir telpas platums?")
garums = input("Kads ir telpas garums?")
augstums = input("Kads ir telpas augstums?")
print("Telpas tilpums ir", round(float(garums)*float(platums)*float(augstums),2))

print("Tresais uzdevums")
c = input("Norâdiet temperaturu pec Celsija skalas")
print("Temperatura pec Farenheita ir", round(float(32+float(c)*(9/5),2)))
