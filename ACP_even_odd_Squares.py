squares = [x**2 for x in range(1, 6)]

even_squares = [x for x in squares if x % 2 == 0]
odd_squares = [x for x in squares if x % 2 != 0]

print("Squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)