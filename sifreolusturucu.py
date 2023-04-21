import random
import string

def generate_password(length, include_digits=True, include_symbols=True):
    """
    Generates a random password with the specified length.
    By default, the password will include digits and symbols.
    """
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Örnek kullanım
length = int(input("Şifre uzunluğunu girin: "))
include_digits = input("Sayılar dahil olsun mu? (E/H): ").lower() == 'e'
include_symbols = input("Semboller dahil olsun mu? (E/H): ").lower() == 'e'
password = generate_password(length, include_digits, include_symbols)
print("Oluşturulan şifre:", password)

input("Programı kapatmak için Enter tuşuna basın...")
