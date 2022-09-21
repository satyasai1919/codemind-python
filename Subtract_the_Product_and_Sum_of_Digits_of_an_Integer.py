n=int(input())
s=0
s1=1
while n>0:
    r=n%10
    s+=r
    s1*=r
    result=s1-s
    n=n//10
print(result)