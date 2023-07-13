#Adding sum of all even numbers from 1 to 100 including 1 & 100

Addition = 0

for n in range(2, 101, 2):
    Addition += n
print(Addition)

Addition2 = 0
for m in range(1, 101):
    if m % 2 == 0:
        Addition2 += m
print(Addition2)