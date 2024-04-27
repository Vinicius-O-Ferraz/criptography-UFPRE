#Atividade 3
from random import randint
from collections import Counter
import math
from activity1 import Alphabet
reload(activity1)

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

key = randint(0,26)
alphabet = Alphabet.charRange('a','z')
LETTER_FREQUENCY_PTBR = {
                    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99,'e':12.57,'f':1.02,'g':1.30,'h':1.28,'i':6.18,'j':0.40,
                    'k':0.02,'l':2.78,'m':4.74,'n':5.05,'o':10.73,'p':2.52,'q':1.20,'r':6.53,'s':7.81,'t':4.34,'u':4.63,
                    'v':1.67,'w':0.01,'x':0.21,'y':0.01,'z':0.47
                    }

def caesaerCypher(message, key):
     return Alphabet.offset(message,key)

def difference(message):
    counter = Counter(message)
    return sum([abs(counter.get(letter, 0) * 100 / len(message) - LETTER_FREQUENCY_PTBR[letter]) for letter in
                alphabet]) / len(alphabet)

def breakCipher(cipherText):
    lowest_difference = math.inf
    encryption_key = 0

    for key in range(1, len(alphabet)):
        current_plain_text = caesaerCypher(cipherText, - key)
        current_difference = difference(current_plain_text)

        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key

    return encryption_key

cipher = Alphabet.clearText(stringMessage)
decript = caesaerCypher(cipher, -key)
print(key)
print(breakCipher(cipher))
