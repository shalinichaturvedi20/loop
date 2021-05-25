num=int(input("enter the number"))
i=0
while i<=num:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    while j>0:
        print(j,end=" ")
        j=j-1
    print()
    i=i+1   