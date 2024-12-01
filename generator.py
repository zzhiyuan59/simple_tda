import random

# Generate a list of 10 random (int, int) pairs
random_pairs = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]

print(random_pairs)
