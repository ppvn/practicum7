count = 0
for i in range(100, 1000):
    if i % 17 == 0:
        print(i,end=' ')
        count += 1

print('\nКоличество трехзначных чисел, которые делятся на 17:', count)
