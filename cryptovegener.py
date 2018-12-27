#Vigenere crypting program

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","à","ç","é","è","ê",
            "ë","â","ä","ù","û","ü","ô","ö","ÿ","ù","ò","ì","î","ï",",",":",";",".","?",
            "!","/","+","=","'","(",")"," ","-","0","1","2","3","4","5","6","7","8","9"]
dicoAlphabet = {0 : ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
                     "t","u","v","w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L",
                     "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","à","ç","é","è","ê",
                     "ë","â","ä","ù","û","ü","ô","ö","ÿ","ù","ò","ì","î","ï",",",":",";",".","?",
                     "!","/","+","=","'","(",")"," ","-","0","1","2","3","4","5","6","7","8","9"]}

#Create all the different alphabets
for loop in range(1, 95):
    alphabet.append(alphabet[0])
    del alphabet[0]
    dicoAlphabet[loop] = alphabet[:]
alphabet.append(alphabet[0])
del alphabet[0]


#Function to encrypt
def encrypt(clef, motACrypter):
    #Create a list of the message to encrypt
    listeMotACrypter = [lettre for index, lettre in enumerate(motACrypter)]
    
    #Adjust the length of the key to the length of the message
    listeClef = []
    boucle = True
    while boucle:
        for loop in range(len(clef)):
            listeClef.append(clef[loop])
            if len(listeMotACrypter) == len(listeClef):
                boucle = False
                break   
    
    #Find the indexs of the letters from the message         
    listeIndexMotACrypter = [loop2 for loop1 in range(len(listeMotACrypter)) for loop2 in range(len(alphabet)) if listeMotACrypter[loop1] == alphabet[loop2]]
    
    #Find the indexs of the letters from the key  
    listeIndexVraiClef = [loop2 for loop1 in range(len(listeClef)) for loop2 in range(len(alphabet)) if listeClef[loop1] == alphabet[loop2]]
    
    #Use indexs find above to crypt each character of the message   
    listeMotCrypter = [dicoAlphabet[listeIndexVraiClef[loop]][listeIndexMotACrypter[loop]] for loop in range(len(listeMotACrypter))]
    
    motCrypter = "".join(listeMotCrypter)
    print(motCrypter, "    is the crypted message")
    
    
#Function to decrypt
def decrypt(clef, motADecrypter):
    #Create a list of the message to decrypt
    listeMotADecrypter = [lettre for index, lettre in enumerate(motADecrypter)]
       
    #Adjust the length of the key to the length of the message
    listeClef = []
    boucle = True
    while boucle:
        for loop in range(len(clef)):
            listeClef.append(clef[loop])
            if len(listeMotADecrypter) == len(listeClef):
                boucle = False
                break
    
    #Find the indexs of the letters from the key  
    listeIndexVraiClef = [loop2 for loop1 in range(len(listeClef)) for loop2 in range(len(alphabet)) if listeClef[loop1] == alphabet[loop2]]
    
    #Find the indexs of the decrypted letters
    listeIndexMotDecrypter = [loop2 for loop1 in range(len(listeMotADecrypter)) for loop2 in range(len(alphabet)) if dicoAlphabet[loop2][listeIndexVraiClef[loop1]] == listeMotADecrypter[loop1]]
    
    #Create a list of all the letters decrypted
    listeMotDecrypter = [alphabet[listeIndexMotDecrypter[loop]] for loop in range(len(listeIndexMotDecrypter))]
    
    #Create the decrypted message from the list
    motDecrypter = "".join(listeMotDecrypter)
    print(motDecrypter, "    is the decrypted message")
  
reponse = str(input("Would you like to encrypt or decrypt : (e/d)\n"))  
if reponse == "e":      
    encrypt(str(input("key\n")), str(input("message to encrypt\n")))
elif reponse == "d":
    decrypt(str(input("key\n")), str(input("message to decrypt\n")))