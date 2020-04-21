count = 0

for c in range(1, 10):
    if c % 2 == 0:
        count += 1
        print(c)

print(f"You have {count} even numbers")
