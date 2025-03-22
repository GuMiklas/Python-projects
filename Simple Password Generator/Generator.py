import random
import string

print('Password Generator')

chars = string.ascii_letters + string.digits + string.punctuation
number = int(input('Enter the number of passwords:'))
length = int(input('Enter the length of passwords:'))
print('Generating passwords...')

for pw in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)