num=int(input("enter the number"))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(" ",end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("1",end=" ")
        star=star-1
    print()
    row+=1 
print()    