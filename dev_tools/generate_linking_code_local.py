import string
import random

def generate_random_string(length):
  characters = string.ascii_letters + string.digits
  similar_chars = [('I', 'l', '1'), ('0', 'O'), ('5', 'S'), ('2', 'Z'), ('8', 'B')]

  while True:
    random_string = ''.join(random.choice(characters) for _ in range(length))
    if not any(all(char in random_string for char in group) for group in similar_chars):
      return random_string
    
for i in range(10):
  print(generate_random_string(12))