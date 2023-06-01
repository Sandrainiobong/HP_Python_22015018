for m in range(1, 101):
    if m % 3 == 0 and m % 5 == 0:
        print("couples", end=", ")
    elif m % 3 == 0:
        print("boys", end=", ")
    elif m % 5 == 0:
        print("girls", end=", ")
    else:
        print(m, end=", ")
   