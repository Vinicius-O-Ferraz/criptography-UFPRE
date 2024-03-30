class cipher:

    def __init__(self,message:str):
        self.message = message.upper().replace(" ","")

    def encrypt(self):

        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        cipherAlphabet = ['aaaaa','aaaab','aaaba','aaabb','aabaa','aabab','aabba','aabbb','abaaa','abaaa','abaab','ababa','ababb','abbaa','abbab','abbba','abbbb','baaaa','baaab','baaba','baabb','baabb','babaa','babab','babba','babbb']

        message = ''

        for c in range(len(self.message)):
            for d in range(len(alphabet)):
                if self.message[c] == alphabet[d]:
                    message = message + " " + cipherAlphabet[d]

        self.message = message

        return self.message

    def decrypt(self):

        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        cipherAlphabet = ['aaaaa','aaaab','aaaba','aaabb','aabaa','aabab','aabba','aabbb','abaaa','abaaa','abaab','ababa','ababb','abbaa','abbab','abbba','abbbb','baaaa','baaab','baaba','baabb','baabb','babaa','babab','babba','babbb']

        decrypted_message = ''

        # Iterate through each "word" in the encrypted message
        for cipher_word in self.message.split():
            decrypted_letter = ''

            # Iterate through each cipher pattern
            for i, cipher_pattern in enumerate(cipherAlphabet):
                if cipher_word == cipher_pattern:
                    decrypted_letter = alphabet[i]  # Find corresponding letter
                    break  # No need to continue searching

            decrypted_message += decrypted_letter  # Build decrypted message

        self.message = decrypted_message.strip()  # Update message attribute
        return self.message

cifra = cipher('STRIKE NOW')
print(cifra.message)
cifra.encrypt()
print(cifra.message)
cifra.decrypt()
print(cifra.message)



