goodText = "yummy" #str
print(goodText)
longText = goodText *3 #str
print(longText)
skaitlis = 123 #int
decSkaitlis = 123.45 #float
pareizi = True #bool
a = type(decSkaitlis)
print(a, " tips ir", type(a))
print(goodText, " tips is", type(goodText))
print(decSkaitlis, " tips ir", type(decSkaitlis))
print(pareizi, " tips is", type(pareizi))
kaSauc = input("Sveiki, batereiki, ka Tevi sauc?") # lietojot input viener bus ka teksts
print("Labdien", kaSauc)
print(type(kaSauc))

cikGadi = input("Cik Tev gadi?")
print("gadu tips ir", type(cikGadi))
cikGadi = int(cikGadi)
print("gadu tips parveidots ir", type(cikGadi))

number = 123.55555
rounded = int(number)
print(number, "apals", rounded) 
print("parasta apalosana", round(number))
print("apalosana ar komatu", round(number,3))
#maina datu tipu no int uz float
number = round(number,2)
print("jaunais skaitlis",number)

a = 5
b = 1
c = a + a
c +=3 # c = c+3
print (f"teksts, tâlak neteksts {2+2} un atkal teksts")
