n=int(input("enter the number"))
i=1
s=0
while i<=n:
    if n%i==0:
        print(i)
        s=s+1
    i=i+1
if s==2:
    print("it is prime number")
else:
    print("it is not prime number") 
    i=i+1           






    

    