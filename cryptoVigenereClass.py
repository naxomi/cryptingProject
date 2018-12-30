class Vigenere:
    def __init__(self, key):
        self.__key = str(key)

        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
                    "t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L",
                    "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","à","ç","é","è","ê",
                    "ë","â","ä","ù","û","ü","ô","ö","ÿ","ù","ò","ì","î","ï",",",":",";",".","?",
                    "!","/","+","=","'","(",")"," ","-","0","1","2","3","4","5","6","7","8","9"]
        self.dictionnaryAlphabet = {0 : ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
                             "t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L",
                             "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","à","ç","é","è","ê",
                             "ë","â","ä","ù","û","ü","ô","ö","ÿ","ù","ò","ì","î","ï",",",":",";",".","?",
                             "!","/","+","=","'","(",")"," ","-","0","1","2","3","4","5","6","7","8","9"]} 
        #Create all the different alphabets
        for loop in range(1, len(self.alphabet)):
            self.alphabet.append(self.alphabet[0])
            del self.alphabet[0]
            self.dictionnaryAlphabet[loop] = self.alphabet[:]
        self.alphabet.append(self.alphabet[0])
        del self.alphabet[0] 
          
    def Encryption(self, word):
                
        self.wordToCrypt = str(word)
        self.listWordToCrypt = [letter for index, letter in enumerate(self.wordToCrypt)]
        
        #Adjust the length of the key to the length of the message
        listKey = []
        self.__listKey = listKey
        length = True
        while length:
            for loop in range(len(self.__key)):
                self.__listKey.append(self.__key[loop])
                if len(self.listWordToCrypt) == len(self.__listKey):
                    length = False
                    break
        #Find the indexs of the letters from the message         
        self.listIndexWordToCrypt = [loop2 for loop1 in range(len(self.listWordToCrypt)) for loop2 in range(len(self.alphabet)) if self.listWordToCrypt[loop1] == self.alphabet[loop2]]
        
        #Find the indexs of the letters from the key  
        self.__listIndexKey = [loop2 for loop1 in range(len(self.__listKey)) for loop2 in range(len(self.alphabet)) if self.__listKey[loop1] == self.alphabet[loop2]]
        
        #Use indexs find above to crypt each character of the message   
        self.listCryptedWord = [self.dictionnaryAlphabet[self.__listIndexKey[loop]][self.listIndexWordToCrypt[loop]] for loop in range(len(self.listWordToCrypt))]
        
        self.cryptedWord = "".join(self.listCryptedWord)
      
    def Decryption(self, word):   
        
        self.wordToDecrypt = str(word)
        #Create a list of the message to decrypt
        self.listWordToDecrypt = [letter for index, letter in enumerate(self.wordToDecrypt)]
           
        #Adjust the length of the key to the length of the message
        listKey = []
        self.__listKey = listKey
        length = True
        while length:
            for loop in range(len(self.__key)):
                self.__listKey.append(self.__key[loop])
                if len(self.listWordToDecrypt) == len(self.__listKey):
                    length = False
                    break
        
        #Find the indexs of the letters from the key  
        self.__listIndexKey = [loop2 for loop1 in range(len(self.__listKey)) for loop2 in range(len(self.alphabet)) if self.__listKey[loop1] == self.alphabet[loop2]]
        
        #Find the indexs of the decrypted letters
        self.listIndexWordToDecrypt = [loop2 for loop1 in range(len(self.listWordToDecrypt)) for loop2 in range(len(self.alphabet)) if self.dictionnaryAlphabet[loop2][self.__listIndexKey[loop1]] == self.listWordToDecrypt[loop1]]
        
        #Create a list of all the letters decrypted
        self.listWordDecrypted = [self.alphabet[self.listIndexWordToDecrypt[loop]] for loop in range(len(self.listIndexWordToDecrypt))]
        
        #Create the decrypted message from the list
        self.wordDecrypted = "".join(self.listWordDecrypted)
                
vigenere1 = Vigenere(input("Enter your key : "))

ask = str(input("Would you like to encrypt or decrypt : (e/d)\n"))  
if ask == "e":      
    vigenere1.Encryption(input("Message to encrypt : "))
    print(vigenere1.cryptedWord)
elif ask == "d":
    vigenere1.Decryption(input("Message to decrypt : "))
    print(vigenere1.wordDecrypted)
