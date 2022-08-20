n=int(input())
s=n**2 
sd=0
while s>0:
    sd=sd+s%10
    s=s//10 
if (n==sd):
    print("Neon Number")
else:
    print("Not Neon Number")