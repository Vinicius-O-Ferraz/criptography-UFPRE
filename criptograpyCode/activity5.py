"""
Esta atividade foi feita por Vinícius Ferraz e Heitor Leonny

Nela foi desenvolvido a cifragem e decifragem por meio da cifra de Vignére.

A mensagem é uma frase do Hobbit e a senha é selecionada aleatoriamente de um conjunto pré-definido de palavras.

Depois que a senha é escolhida ela é extendida por toda a mensagem e é feita a cifragem de Vignére.
"""

import random

def clear_text(text):
    return ''.join(filter(str.isalpha, text)).lower()

def caesar_cipher(alphabet, shift, decrypt=False):
    if decrypt:
        shift = -shift
    return alphabet[shift:] + alphabet[:shift]

def generate_tabula_recta(alphabet):
    return [caesar_cipher(alphabet, i) for i in range(len(alphabet))]

def expand_key(key, length):
    return (key * (length // len(key)) + key[:length % len(key)]).upper()

def encrypt_vigenere(message, key, tabula_recta, alphabet):
    encrypted_message = []
    expanded_key = expand_key(key, len(message))

    for m_char, k_char in zip(message, expanded_key):
        row = alphabet.index(k_char.lower())
        col = alphabet.index(m_char)
        encrypted_message.append(tabula_recta[row][col])

    return ''.join(encrypted_message)

def decrypt_vigenere(encrypted_message, key, tabula_recta, alphabet):
    decrypted_message = []
    expanded_key = expand_key(key, len(encrypted_message))

    for e_char, k_char in zip(encrypted_message, expanded_key):
        row = alphabet.index(k_char.lower())
        col = tabula_recta[row].index(e_char)
        decrypted_message.append(alphabet[col])

    return ''.join(decrypted_message)

alphabet = charRange("a", "z")
tabula_recta = generate_tabula_recta(alphabet)

random_keys = [
    "Thorin", "Balin", "Dwalin", "Fili", "Kili", "Dori",
    "Nori", "Ori", "Oin", "Gloin", "Bifur", "Bofur",
    "Bombur"
]

key = random.choice(random_keys).upper()
print("A chave selecionada foi: " + key)

string_message =  "Um mago nunca se atrasa, Frodo Bolseiro. Nem se adianta; ele chega exatamente quando pretende. "
clear_message = clear_text(string_message)

encrypted_message = encrypt_vigenere(clear_message, key, tabula_recta, alphabet)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt_vigenere(encrypted_message, key, tabula_recta, alphabet)
print(f"Decrypted Message: {decrypted_message}")
