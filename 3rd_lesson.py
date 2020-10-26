True, False
print(2*2==4) # divas vienadîbas zimes pârbauda, vai sakariba izpildas
#do stuff
print("All done")
isCalcGood = 3*3==9 # we evaluate from the right side to left
isCalcStillGood = 2*2==5
a = 4
b = 5
c = 2
print(a==2*2)
isCalcStillGood = a == 2*2
print("This calculation is", a == c*c)
# in python types can change
# c = a ==2*2 # c is bad name for boolean type
# booleans usually start with "is"
print(a!=b, 4>4, a<3, a==b, a<=4, a>=4)
a = -500
print(a!=b, 4>4, a<3, a==b, a<=4, a>=4)
c = 9000
d = 9000
e = 9000
print (c == d) # we check value equality
print (c is d) # we check whether c and d point to the same value

print("Vardi")
myName = "Valdis"
friendName = "Voldemars"
print(myName > friendName) #jo o ir pec a, pec ASCII tabulas, stringi tiek salîdzinâti pçc leksografikas
print("a pozicija", ord("a"))
print("o pozicija", ord("o"))
print(len(myName) > len(friendName), len(myName), len(friendName), myName, friendName)
print(True and True) # in python is used and (not &&)
print (5>4 and 10<4) # ja viena no pusem nepareizi, tad gala rezultâts ir false
#tikko ir viens false tâ pythons tâlak nepârbauda, jo tâ pat gala rezultâts bûs false
print("one false, all false")
print(False and False)
print(True and False)
print(False and True)
print("one true = result true, searches for first true")
print("False or False", False or False)
print("True or False", True or False)
print("True or True", True or True)
print("False or True", False or True)
a = 25
b = 10
print(a > 24 or b>1_000) # for large number can use _ as seperator
print("" or 0 or False) # "" and 0 are Falsy values
print("" or 9000 or False or 1) # 1 are Truthy values, izvada pirmo pareizo
print("Valdis" and 9000 and True and 45) # and izvada pedejo
print("Valdis" and 9000 and True)
print("Valdis" and True and 9000)
print("0.1 + 0.2==0.3", 0.1 + 0.2, 0.1 + 0.2==0.3)
print("rounded 0.1 + 0.2==0.3", round(0.1 + 0.2,2), round(0.1 + 0.2,2)==0.3)

a = 10

b = 20

c = a and b