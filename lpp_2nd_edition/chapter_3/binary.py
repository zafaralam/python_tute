# binary.py
n = 39
remainders = []
while n > 0:
    remainders.insert(0, n % 2)
    n //= 2

print(remainders)
