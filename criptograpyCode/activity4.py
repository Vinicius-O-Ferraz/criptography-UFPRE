"""  

  Este código é a implementação da cifra de Vignére que é uma cifra que funciona tal como a cifra de deslocamento só que com uma palavra chave ao invés de um número de casas de deslocamento.

  Aqui é gerada a tabela recta que é usada para cifragem e decifragem da mensagem. Além disso, a chave é sorteada aleatoriamenta a cada vez que o programa for executado

"""

import random

# Função para limpar a mensagem
def clear_text(text):
    return ''.join(filter(str.isalpha, text)).lower()

# Função para gerar o alfabeto
def char_range(start, end):
    return [chr(i) for i in range(ord(start), ord(end) + 1)]

# Função para gerar a tábula reta
def generate_tabula_recta(alphabet):
    return [caesar_cipher(alphabet, i).upper() for i in range(len(alphabet))]

# Função para expandir a chave
def expand_key(key, length):
    return (key * (length // len(key)) + key[:length % len(key)]).upper()

# Função para criptografar a mensagem usando a tábula reta como array de strings
def encrypt_vigenere(message, key, tabula_recta, alphabet):
    encrypted_message = []
    expanded_key = expand_key(key, len(message))
    
    for m_char, k_char in zip(message, expanded_key):
        row = alphabet.index(k_char.lower())
        col = alphabet.index(m_char)
        encrypted_message.append(tabula_recta[row][col])
    
    return ''.join(encrypted_message)

# Função para descriptografar a mensagem usando a tábula reta como array de strings
def decrypt_vigenere(encrypted_message, key, tabula_recta, alphabet):
    decrypted_message = []
    expanded_key = expand_key(key, len(encrypted_message))
    
    for e_char, k_char in zip(encrypted_message, expanded_key):
        row = alphabet.index(k_char.lower())
        col = tabula_recta[row].index(e_char)
        decrypted_message.append(alphabet[col])
    
    return ''.join(decrypted_message)

# Main code
alphabet = char_range("a", "z")

# Gerando a tábula reta como array de strings
tabula_recta = [
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'BCDEFGHIJKLMNOPQRSTUVWXYZA', 'CDEFGHIJKLMNOPQRSTUVWXYZAB', 'DEFGHIJKLMNOPQRSTUVWXYZABC', 
    'EFGHIJKLMNOPQRSTUVWXYZABCD', 'FGHIJKLMNOPQRSTUVWXYZABCDE', 'GHIJKLMNOPQRSTUVWXYZABCDEF', 'HIJKLMNOPQRSTUVWXYZABCDEFG', 
    'IJKLMNOPQRSTUVWXYZABCDEFGH', 'JKLMNOPQRSTUVWXYZABCDEFGHI', 'KLMNOPQRSTUVWXYZABCDEFGHIJ', 'LMNOPQRSTUVWXYZABCDEFGHIJK', 
    'MNOPQRSTUVWXYZABCDEFGHIJKL', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'OPQRSTUVWXYZABCDEFGHIJKLMN', 'PQRSTUVWXYZABCDEFGHIJKLMNO', 
    'QRSTUVWXYZABCDEFGHIJKLMNOP', 'RSTUVWXYZABCDEFGHIJKLMNOPQ', 'STUVWXYZABCDEFGHIJKLMNOPQR', 'TUVWXYZABCDEFGHIJKLMNOPQRS', 
    'UVWXYZABCDEFGHIJKLMNOPQRST', 'VWXYZABCDEFGHIJKLMNOPQRSTU', 'WXYZABCDEFGHIJKLMNOPQRSTUV', 'XYZABCDEFGHIJKLMNOPQRSTUVW', 
    'YZABCDEFGHIJKLMNOPQRSTUVWX', 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
]

random_keys = [
    "Thorin", "Balin", "Dwalin", "Fili", "Kili", "Dori",
    "Nori", "Ori", "Oin", "Gloin", "Bifur", "Bofur",
    "Bombur"
]

key = random.choice(random_keys).upper()

# Mensagem a ser criptografada
string_message = "This is a secret message"
clear_message = clear_text(string_message)

# Criptografar a mensagem
encrypted_message = encrypt_vigenere(clear_message, key, tabula_recta, alphabet)
print(f"Encrypted Message: {encrypted_message}")

# Descriptografar a mensagem
decrypted_message = decrypt_vigenere(encrypted_message, key, tabula_recta, alphabet)
print(f"Decrypted Message: {decrypted_message}")
