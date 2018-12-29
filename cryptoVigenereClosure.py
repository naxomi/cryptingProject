#Vigenere crypting program

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","à","ç","é","è","ê",
            "ë","â","ä","ù","û","ü","ô","ö","ÿ","ù","ò","ì","î","ï",",",":",";",".","?",
            "!","/","+","=","'","(",")"," ","-","0","1","2","3","4","5","6","7","8","9"]
dictionnaryAlphabet = {0 : ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
                     "t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L",
                     "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","à","ç","é","è","ê",
                     "ë","â","ä","ù","û","ü","ô","ö","ÿ","ù","ò","ì","î","ï",",",":",";",".","?",
                     "!","/","+","=","'","(",")"," ","-","0","1","2","3","4","5","6","7","8","9"]}

#Create all the different alphabets
for loop in range(1, len(alphabet)):
    alphabet.append(alphabet[0])
    del alphabet[0]
    dictionnaryAlphabet[loop] = alphabet[:]
alphabet.append(alphabet[0])
del alphabet[0]

def helloIsTheKeyToEncrypt(wordToCrypt, key="hello"):
    #Fonction to encrypt
    def encrypt():
        #Create a list of the message to encrypt
        listWordToCrypt = [letter for index, letter in enumerate(wordToCrypt)]
        
        #Adjust the length of the key to the length of the message
        listKey = []
        length = True
        while length:
            for loop in range(len(key)):
                listKey.append(key[loop])
                if len(listWordToCrypt) == len(listKey):
                    length = False
                    break   
        
        #Find the indexs of the letters from the message         
        listIndexWordToCrypt = [loop2 for loop1 in range(len(listWordToCrypt)) for loop2 in range(len(alphabet)) if listWordToCrypt[loop1] == alphabet[loop2]]
        
        #Find the indexs of the letters from the key  
        listIndexKey = [loop2 for loop1 in range(len(listKey)) for loop2 in range(len(alphabet)) if listKey[loop1] == alphabet[loop2]]
        
        #Use indexs find above to crypt each character of the message   
        listCryptedWord = [dictionnaryAlphabet[listIndexKey[loop]][listIndexWordToCrypt[loop]] for loop in range(len(listWordToCrypt))]
        
        cryptedWord = "".join(listCryptedWord)
        print("This is the crypted message >>>", cryptedWord)
    return encrypt()
        
def helloIsTheKeyToDecrypt(wordToDecrypt, key="salut"):
    #Function to decrypt
    def decrypt():
        #Create a list of the message to decrypt
        listWordToDecrypt = [letter for index, letter in enumerate(wordToDecrypt)]
           
        #Adjust the length of the key to the length of the message
        listKey = []
        length = True
        while length:
            for loop in range(len(key)):
                listKey.append(key[loop])
                if len(listWordToDecrypt) == len(listKey):
                    length = False
                    break
        
        #Find the indexs of the letters from the key  
        listIndexKey = [loop2 for loop1 in range(len(listKey)) for loop2 in range(len(alphabet)) if listKey[loop1] == alphabet[loop2]]
        
        #Find the indexs of the decrypted letters
        listIndexWordToDecrypt = [loop2 for loop1 in range(len(listWordToDecrypt)) for loop2 in range(len(alphabet)) if dictionnaryAlphabet[loop2][listIndexKey[loop1]] == listWordToDecrypt[loop1]]
        
        #Create a list of all the letters decrypted
        listWordDecrypted = [alphabet[listIndexWordToDecrypt[loop]] for loop in range(len(listIndexWordToDecrypt))]
        
        #Create the decrypted message from the list
        wordDecrypted = "".join(listWordDecrypted)
        print("This is the decrypted message >>> ", wordDecrypted)
    return decrypt()


reponse = str(input("Would you like to encrypt or decrypt : (e/d)\n"))  
if reponse == "e":      
    helloIsTheKeyToEncrypt(str(input("Enter your message to encrypt : \n")))
elif reponse == "d":
    helloIsTheKeyToDecrypt(str(input("Enter your message to decrypt : \n")))