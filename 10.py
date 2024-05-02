t = (float(input()))
count = 0
while True:
    temp = float(input())
    if temp == 0:
        break
    if temp < t:
        count += 1
    t = temp
print(count)
