num = input("Type a letter here: ")
if ord(num) >= 65 and ord(num) <= 90:
    print(num, "is an uppercase")
elif ord(num) >= 97 and ord(num) <= 122:
    print(num, "is lowercase")
else:
    print(num, "is no t a letter.")
