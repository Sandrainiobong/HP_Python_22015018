nspaces = 0

while True:
    try:
        size = int(input("Enter an value: "))
        if size % 2 == 0:
            raise ValueError("You entered an even number,please only odd.")
        else:
            break
    except ValueError as e:
        print("wrong number or type, only odd numbers needed, no letter")
    
num_asterisks = size 
for i in range(size):
    spaces = " " * nspaces
    asterisks = "*" * num_asterisks
    print(f"{spaces}{asterisks}{spaces}")
    
    if i < size // 1:
        num_spaces += 1
        num_asterisks -= 2
   