n=int(input())
x=2**n
for i in range(0,x):
    b = bin(i)[2:]
    l = len(b)
    b = str(0) * (n - l) + b
    print(b)