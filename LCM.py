a,b=map(int,input().split())
i=1
while i>0:
    r=a*i
    if r%b==0:
        print(r)
        break
    i=i+1