a = int(input("Please enter 1st number"))
b = int(input("Please enter 2nd number"))
c = int(input("Please enter 3rd number"))

print("Numbers in ascending order are")

if a<b and a<c:
    print (a)
    if b<c:
        print (b,"\n",c,sep="")
    else:
        print (c,"\n",b,sep="")
else:
    if b<a and b<c:
        print (b)
        if a<c:
            print (a,"\n",c,sep="")
        else:
            print (c,"\n",a,sep="")
    else:
        print(c)
        if a<b:
            print (a,"\n",b,sep="")
        else:
            print (b,"\n",a,sep="")