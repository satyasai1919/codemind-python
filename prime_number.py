num = int(input())
y=num//2
if num > 1:
    for i in range(2,y+1):
        if (num % i) == 0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")
