import random
import string

print("🔐 Advanced Password Generator")

length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ")
use_digits = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = ""

if use_letters == 'y':
    characters += string.ascii_letters
if use_digits == 'y':
    characters += string.digits
if use_symbols == 'y':
    characters += string.punctuation

if characters == "":
    print("❌ You must select at least one option!")
else:
    password = "".join(random.choice(characters) for i in range(length))
    print("✅ Your strong password is:", password)