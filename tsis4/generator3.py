def div_by_three_and_four(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in div_by_three_and_four(50):
    print(num)
