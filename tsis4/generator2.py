def even_numbers(n):
    # Generate even numbers between 0 and n
    for i in range(0, n+1, 2):
        yield i

# Get input from console
n = int(input("Enter a number: "))

# Use generator to print even numbers in comma separated form
print(*even_numbers(n), sep=', ')
