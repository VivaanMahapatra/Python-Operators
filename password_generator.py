import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits

all_characters = lowercase + uppercase + numbers

length = 10

password_list = random.sample(all_characters, length)
random.shuffle(password_list)

password = "".join(password_list)

print("Generated Password:", password)