#Atividade 1

class Alphabet:

    """
    A class containing methods for working with alphabets and text manipulation.
    """
    
    @staticmethod
    def charRange(c1: chr,c2: chr)->list:

        """
       Generates a list of characters between two given characters (inclusive).

       Args:
           c1: The first character in the range.
           c2: The second character in the range.

       Returns:
           A list of characters between c1 and c2.
       """
        
        list = []
        for i in range(ord(c1),ord(c2)+1):
            list = list + [chr(i)]

        return list
    
    @staticmethod
    def checkIfItsAlphabetic(message:str)->bool:

        """
       Checks if a string contains only alphabetical characters.

       Args:
           message: The string to check.

       Returns:
           True if all characters in the message are alphabetical, False otherwise.
       """
         
        if not all(caracter.isalpha() for caracter in message):
            return False
                     
        else:
            return True

    @staticmethod
    def offsetV1(message: str, value: int) -> str:

        """
       Applies a Caesar Cipher shift to a string, preserving only alphabetical characters.

       Args:
           message: The string to shift.
           value: The amount to shift each character by.

       Returns:
           The shifted string, containing only alphabetical characters.
       """
        
        if Alphabet.checkIfItsAlphabetic(message):
            offseted_message = ''
            for char in message:
                
                newOrd = ord(char) + value 
                offseted_message += chr(newOrd)

            return offseted_message
        
        else:
            return 'The written input is invalid'
    
    @staticmethod
    def offsetV2(message: str, value: int) -> str:

        """
       Applies a Caesar Cipher shift to a string, preserving both alphabetical and non-alphabetical characters.

       Args:
           message: The string to shift.
           value: The amount to shift each character by.

       Returns:
           The shifted string, preserving all characters.
       """
        message = message.replace(' ','').upper()

        offseted_message = ''

        for i in range(len(message)):
            
            if message[i].isalpha():
                offseted_message = offseted_message + Alphabet.offsetV1(message[i],value)
        
            else:
                offseted_message = offseted_message + message[i]

        return offseted_message

    
    @staticmethod
    def clearText(message:str)->str:

        """
       Removes all non-alphabetical characters from a string.

       Args:
           message: The string to clear.

       Returns:
           The string containing only alphabetical characters.
       """

        offseted_message = ''
        message = message.upper()

        for i in range(len(message)):

            if  message[i].isalpha():
                if message[i] in ["Á", "À", "Ã", "Ã", "Ä"]:
                    offseted_message += "A"
                elif message[i] in ["É", "È", "Ê", "Ë"]:
                    offseted_message += "E"
                elif message[i] in ["Í", "Ì", "Î", "Ï"]:
                    offseted_message += "I"
                elif message[i] in ["Ó", "Ò", "Ô", "Õ", "Ö"]:
                    offseted_message += "O"
                elif message[i] in ["Ú", "Ù", "Û", "Ü"]:
                    offseted_message += "U"
                elif message[i] in ["Ç"]:
                    offseted_message += "C"
                else:
                    offseted_message += message[i]

        return offseted_message



