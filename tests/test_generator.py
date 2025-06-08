import pytest
import string
from generator.generator import generate_password

def test_password_default_length():
    password = generate_password()
    assert len(password) == 8

def test_password_custom_length():
    length = 16
    password = generate_password(length)
    assert len(password) == length

def test_password_only_uppercase():
    password = generate_password(12, use_upper=True, use_lower=False, use_digits=False, use_symbols=False)
    assert all(c in string.ascii_uppercase for c in password)

def test_password_only_lowercase():
    password = generate_password(12, use_upper=False, use_lower=True, use_digits=False, use_symbols=False)
    assert all(c in string.ascii_lowercase for c in password)

def test_password_only_digits():
    password = generate_password(12, use_upper=False, use_lower=False, use_digits=True, use_symbols=False)
    assert all(c in string.digits for c in password)

def test_password_only_symbols():
    password = generate_password(12, use_upper=False, use_lower=False, use_digits=False, use_symbols=True)
    assert all(c in string.punctuation for c in password)

def test_password_all_character_sets():
    password = generate_password(20, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)

def test_password_randomness():
    pwd1 = generate_password(16)
    pwd2 = generate_password(16)
    assert pwd1 != pwd2  # improvável de serem iguais

def test_invalid_no_charset_selected():
    with pytest.raises(ValueError):
        generate_password(12, use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

def test_minimum_length():
    password = generate_password(1)
    assert len(password) == 1

def test_maximum_length():
    password = generate_password(100)
    assert len(password) == 100
