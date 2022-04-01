# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
res_l = "".join(random.choices(letters, k=nr_letters))
# print(res_l)
res_s = "".join(random.choices(symbols, k=nr_symbols))
res_n = "".join(random.choices(numbers, k=nr_numbers))
res_pwd = res_l + res_s + res_n
print(f"Here is your password medium version: {res_pwd}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pwd = list(res_pwd)
random.shuffle(pwd)
res_pwd2 = "".join(pwd)
print(f"Here is your password strong version: {res_pwd2}")

# instructor version

pwd = ""

for char in range(1, nr_letters + 1):
    pwd += random.choice(letters)
for char in range(1, nr_symbols + 1):
    pwd += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    pwd += random.choice(numbers)
print(pwd)

pwd = list(pwd)
random.shuffle(pwd)
print("".join(pwd))
