class cipher:

    def __init__(self,message:str):

        """
        This class implements a simple Caesar cipher variant with a custom mapping. 
        It encrypts and decrypts messages using a substitution method.
        """

        self.message = message.upper().replace(" ","")

      


    def encrypt(self):

        """
        Encrypts the message using a custom substitution mapping.

        Returns:
        The encrypted message.

        Performs the following:
        - Defines two lists:
            - alphabet: A list containing all uppercase letters.
            - cipherAlphabet: A list containing custom cipher patterns for each letter.
        - Initializes an empty string to store the encrypted message.
        - Iterates over each character in the message:
            - Iterates over the alphabet list to find the corresponding index.
            - If a match is found, appends a space and the cipher pattern from the cipherAlphabet list at that index to the encrypted message string.
        - Updates the message attribute with the encrypted message.
        - Returns the encrypted message.
        """

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

        """
    Decrypts the message using the custom substitution mapping.

    Returns:
      The decrypted message.

    Performs the following:
      - Defines two lists (same as in encrypt):
        - alphabet: A list containing all uppercase letters.
        - cipherAlphabet: A list containing custom cipher patterns for each letter.
      - Initializes an empty string to store the decrypted message.
      - Splits the encrypted message into a list of "words" (each cipher pattern).
      - Iterates over each "word" in the split message:
        - Initializes an empty string to store the decrypted letter.
        - Iterates over the cipherAlphabet list to find a matching pattern.
        - If a match is found, retrieves the corresponding letter from the alphabet list at the same index and breaks the loop (no need to search further).
        - Appends the decrypted letter to the decrypted message string.
      - Removes leading/trailing spaces from the decrypted message and updates the message attribute.
      - Returns the decrypted message.
        """

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



