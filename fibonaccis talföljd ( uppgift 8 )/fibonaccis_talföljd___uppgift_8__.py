a=0
b=1
c=0

while a<40 :
    a+=1
    if a %2 == 0:
        if c>2 or b>2:
            print("tal", a," : ",b, "\n Kvot:",b/c,"\n")
            c+=b
        else:
            print("tal",a," :", b)
            c+=b

    else :
         if c>2 or b>2:
            print("tal", a," : ",c, "\n Kvot:",c/b,"\n")
            b+=c
         else:
            print("tal",a," :", c)
            b+=c
            