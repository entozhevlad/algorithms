import sys
n = int(sys.stdin.readline().strip())
f = 1
for i in range(2,n+1):
    f *= i
    while f%10 == 0:
        f //= 10
    f %= 100000
sys.stdout.write(str(f%10))

