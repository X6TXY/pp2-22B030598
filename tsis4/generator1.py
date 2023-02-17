def squares_generator(N):
    for i in range(1, N+1):
        yield i*i
for square in squares_generator(5):
    print(square)
