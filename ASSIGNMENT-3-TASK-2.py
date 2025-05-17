import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

print("Square root: " + str(num) + ": " + str(square_root))
print("Logarithm: " + str(num) + ": " + str(natural_log))
print("Sine: " + str(num) + " (in radians): " + str(sine_value))
