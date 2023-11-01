import random
my_arr = []
chars = "qwertyuiopasdfghjklzxcvbnm"
symbols = "!@#$%^&*()"
numbers = "1234567890"

for i in range(24):
    my_arr.append(random.choice(numbers))
for i in range(12):
    my_arr.append(random.choice(chars))
    my_arr.append(random.choice(symbols))

final_password = ""
for i in range(len(my_arr)):
    current_char = random.choice(my_arr)
    final_password += current_char
    my_arr.remove(current_char)


print(final_password)