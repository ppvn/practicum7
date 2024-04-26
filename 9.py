n = int(input())
k = int(input())
r = int(input())
count = 1
while n < r:
    n *= k/100 + 1
    count += 1
print(count)
