class Encrypt:
    def __init__(self, key, word):
        self.key = str(key)
        self.wordToCrypt = str(word)
        self.listWordToCrypt = [letter for index, letter in enumerate(self.wordToCrypt)]
        
    def LengthKey(self):
        #Adjust the length of the key to the length of the message
        listKey = []
        length = True
        while length:
            for loop in range(len(self.key)):
                listKey.append(self.key[loop])
                if len(self.listWordToCrypt) == len(listKey):
                    length = False
                    break
        self.listKey = listKey
    
    def Alphabet(self):
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
        
          
    def Encryption(self):
        #Find the indexs of the letters from the message         
        self.listIndexWordToCrypt = [loop2 for loop1 in range(len(self.listWordToCrypt)) for loop2 in range(len(self.alphabet)) if self.listWordToCrypt[loop1] == self.alphabet[loop2]]
        
        #Find the indexs of the letters from the key  
        self.listIndexKey = [loop2 for loop1 in range(len(self.listKey)) for loop2 in range(len(self.alphabet)) if self.listKey[loop1] == self.alphabet[loop2]]
        
        #Use indexs find above to crypt each character of the message   
        self.listCryptedWord = [self.dictionnaryAlphabet[self.listIndexKey[loop]][self.listIndexWordToCrypt[loop]] for loop in range(len(self.listWordToCrypt))]
        
        self.cryptedWord = "".join(self.listCryptedWord)
        

encrypt1 = Encrypt(input("Key : "), input("Message to encrypt : "))
encrypt1.LengthKey()
encrypt1.Alphabet()
encrypt1.Encryption()
print(encrypt1.cryptedWord)
