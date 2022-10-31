a=int(input())
temp=a
rev=0
if a<0:
    a=a*(-1)
while a!=0:
    r=a%10
    rev=rev*10+r
    a=a//10
if temp>0:
    print(rev)
else:
    rev1=rev*(-1)
    print(rev1)
    
