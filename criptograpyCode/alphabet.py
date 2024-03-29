class Alphabet:

    def charRange(c1: chr,c2: chr)->list:
        list = []
        for i in range(ord(c1),ord(c2)+1):
            list = list + [chr(i)]

        return list
    
    def checkIfItsAlphabetic(message:str):
        if not all(caracter.isalpha() for caracter in message):
            return False
                     
        else:
            return True

    def offsetV1(message: str, value: int) -> str:
        
        if Alphabet.checkIfItsAlphabetic(message):
            offseted_message = ''
            for char in message:
                
                newOrd = ord(char) + value 
                offseted_message += chr(newOrd)

            return offseted_message
        
        else:
            return 'The written input is invalid'
        
    def offsetV2(message: str, value: int) -> str:
        offseted_message = ''

        for i in range(len(message)):
            
            if message[i].isalpha():
                offseted_message = offseted_message + Alphabet.offsetV1(message[i],value)
        
            else:
                offseted_message = offseted_message + message[i]

        return offseted_message

    def clearText(message:str)->str:
        offseted_message = ''

        for i in range(len(message)):
            
            if message[i].isalpha():
                offseted_message = offseted_message + message[i]

        return offseted_message
    
message = Alphabet.clearText('vinicius lindao 123456 -=-=-=')
print(message)