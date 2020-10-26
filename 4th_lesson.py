# i = 1
# while i<5:
#     print("i vertiba ir", i)
#     i += 1
# 
# i = 1
# while True:
#     print("i vertiba ir", i)
#     if i>5:
#         break # exits loop
#     i += 1
# 
# continue
i = 1
while i < 10:
    if i % 2 == 0:
        print("Even number!", i)
        i += 1
        continue # means we go to start of the loop immediately
    print("My generic num", i)
    i += 1
    if i >= 7:
        break
print("All done")


i = 0
isEndOfWorld = False
maxCount = 4
while i<maxCount and not isEndOfWorld:
    myInput = input("Enter number or q to quit: ")
    if myInputLower().startswith("q"):
        break
    num = float(myInput)
    print(num, "cubed is", round(num**3, 2))
    if num**3 >9000:
        print("Big result!")
        isEndOfWorld = True
    i += 1
print("This will print after break")
    
    
