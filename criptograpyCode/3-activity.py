#Atividade 3

'''
Parte 1: Cifra de deslocamento

Escreva uma funcao em Python que recebe um texto limpo, isto e, sem acentos nem numeros e nem caracteres especiais e, em seguida, cifra esse texto utilizando a cifra de deslocamento.

Entrada: Mensagem (texto limpo) m e uma chave k ∈ {1, 2, ..., 25}.

Saida: Texto cifrado apenas.

Observacao: Como a forma de cifrar e de decifrar para a Cifra de Deslocamento sao identicas, mudando apenas o sinal da chave, nao e necessario implementar uma funcao de decifracao.'''

from alphabet import Alphabet

test = Alphabet.offsetV2('STRIKE NOW',25) #oddset V2 was been implemented since the begining of the course in the Alphabet class
print(test)

'''
Parte 2: Quebra da cifra de deslocamento

Escreva uma função em Python que recebe um texto limpo, isto é, sem acentos nem números
e nem caracteres especiais e, em seguida, cifra esse texto utilizando a cifra de deslocamento.

Entrada:

Mensagem (texto limpo) m
Uma chave k ∈ {1, 2, ..., 25}

Saída:
Texto cifrado apenas
'''

