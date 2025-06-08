import random
import string

def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Selecione pelo menos um tipo de caractere.")

    return ''.join(random.choice(characters) for _ in range(length))
