n=int(input())
s=n**2
sd=0
while s>0:
    a=s%10
    sd=sd+a
    s=s//10
if(n==sd):
    print('Neon Number')
else:
    print('Not Neon Number')