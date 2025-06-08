import random
import string

def generate_password(length=8):
    characters = string.ascii_letters  # letras maiúsculas + minúsculas
    return ''.join(random.choice(characters) for _ in range(length))
