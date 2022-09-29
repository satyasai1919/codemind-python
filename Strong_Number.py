s=0
num =int(input())
temp =num
while(num):
   i=1
   fact=1
   remainder =num%10
   while(i<=remainder):
      fact=fact*i
      i=i+1
   s= s+fact
   num=num//10
if(s== temp):
   print("The number {0} is a strong number".format(temp))
else:
   print("The number {0} is not a strong number".format(temp))