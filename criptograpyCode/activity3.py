#Atividade 3
from random import randint
from collections import Counter
import math
from activity1 import Alphabet

stringMessage =                     """
De tudo, ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento.

Quero vivê-lo em cada vão momento
E em louvor hei de espalhar meu canto
E rir meu riso e derramar meu pranto
Ao seu pesar ou seu contentamento.

E assim, quando mais tarde me procure
Quem sabe a morte, angústia de quem vive
Quem sabe a solidão, fim de quem ama

Eu possa me dizer do amor (que tive):
Que não seja imortal, posto que é chama
Mas que seja infinito enquanto dure.
"""

stringMessage = stringMessage.lower()

key = randint(0,26)
alphabet = Alphabet.charRange('a','z')
LETTER_FREQUENCY_PTBR = {
                    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99,'e':12.57,'f':1.02,'g':1.30,'h':1.28,'i':6.18,'j':0.40,
                    'k':0.02,'l':2.78,'m':4.74,'n':5.05,'o':10.73,'p':2.52,'q':1.20,'r':6.53,'s':7.81,'t':4.34,'u':4.63,
                    'v':1.67,'w':0.01,'x':0.21,'y':0.01,'z':0.47
                    }

def caesarCypher(message,key,decrypt):
    result = ''
    for char in message:
        if char not in alphabet:
            result += char
            continue
        index = alphabet.index(char.lower())
        if decrypt:
            new_char = alphabet[(index - key) % len(alphabet)]
        else:
            new_char = alphabet[(index + key) % len(alphabet)]
        result += new_char.upper() if char.isupper() else new_char
    return result


def difference(message):
    counter = Counter(message)
    return sum([abs(counter.get(letter, 0) * 100 / len(message) - LETTER_FREQUENCY_PTBR[letter]) for letter in
                alphabet]) / len(alphabet)

def break_cipher(cipher_text):
    lowest_difference = math.inf
    encryption_key = 0

    for key in range(0, len(alphabet)):
        current_plain_text = caesarCypher(cipher_text, key, True)
        current_difference = difference(current_plain_text)

        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key

    return encryption_key

print(stringMessage)
cipher = caesarCypher(stringMessage,key,False)
print(cipher)
decript = caesarCypher(cipher,key,True)
print(break_cipher(cipher))
