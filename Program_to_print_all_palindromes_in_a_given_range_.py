m=int(input())
n=int(input())
for num in range(m,n+1):
    temp = num
    reverse = 0
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print(num,end=' ')