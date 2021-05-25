num=int(input("enyter the number"))
i=1
s=0
while i<num:   
    if num%i==0: 
       print(i) 
       s=s+1
       i=i+1 
print(s)            
if num==s:         
    print("it is perfect number")
else:
    print("it is not perfect number")
    

