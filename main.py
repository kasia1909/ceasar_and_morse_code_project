# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import os
from pathlib import Path


help = "This is the program that can encrypt and decrypt texts. Please provide following arguments in console (after script name): \n \
       1. 'E' - for encrypting or 'D' - for decrypting. \n \
       2. 'C' - for Caesar cipher or  'M' for Morse code. \n \
       3. shift for Caesar cipher (integer number) - in case of Morse code provide any integer \n \
       4. 'path/text_file_name.txt' (it could be only same name of file but file needs to be stored in the same folder as script) - \n \
        please remember that text should contain only spaces and lowercase letters from English alphabet."


# functions for encrypting nad decrypting
def encode_morse(text):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'ą','ć','ę','ł','ń','ó','ś','ż','ź','1','2','3','4','5','6','7','8','9','0']

    b = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..','__',
        '_.','___','.__.','__._','._.','...','_','.._','..._','.__','_.._','_.__','__..',
        '._._','_._..','.._..','._.._','__.__','___.','..._...','__.._.','__.._',
        '.____','..___','...__','...._','.....','_....','__...','___..','____.','_____']

    text = text.lower()
    text2 = ''

    for t in text:
        if(t in a):
            text2 = text2+b[a.index(t)]+' '
        else:
            text2 = text2+t

    return text2.strip()



def decode_morse(text):
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'ą','ć','ę','ł','ń','ó','ś','ż','ź','1','2','3','4','5','6','7','8','9','0']
    b = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..','__',
        '_.','___','.__.','__._','._.','...','_','.._','..._','.__','_.._','_.__','__..',
        '._._','_._..','.._..','._.._','__.__','___.','..._...','__.._.','__.._',
        '.____','..___','...__','...._','.....','_....','__...','___..','____.','_____']

    text = text.lower()
    text2 = ''

    for t in text.split(' '):
        if(t in b):
            text2 = text2+a[b.index(t)]
        elif(t==''):
            text2 = text2+' '
        else:
            text2 = text2+t

    return text2


#caesar cipher

def caesar_encrypt(text,s):
    encryptedText = ""
    for i in range(len(text)):
        C = text[i]
        if C == chr(32): #if C is a space doesnt shift
            encryptedText += C
        elif C.isupper():
            encryptedText += chr((ord(C) +s - ord('A')) % 26 + ord('A'))
        elif C.islower():
            encryptedText += chr((ord(C) +s -ord('a')) % 26 + ord('a'))
    return encryptedText



#caesar decipher

def caesar_decrypt(text,s):
    decryptedText = ""
    for i in range(len(text)):
        C = text[i]
        if C == chr(32): #if C is a space doesnt shift
            decryptedText += C
        elif C.isupper():
            decryptedText += chr((ord(C) -s - ord('A')) % 26 + ord('A'))
        elif C.islower():
            decryptedText += chr((ord(C) -s -ord('a')) % 26 + ord('a'))
    return decryptedText






# calling functions
if len(sys.argv) != 5:
    print('Number of arguments in not correct.')
    print(help)
else:

    text_file_path = sys.argv[4]
    if not os.path.isfile(text_file_path):
        print('Text file does not exist.')
        print(help)
    else:
        txt = Path(text_file_path).read_text()
        #print(txt)

        if sys.argv[1] not in ('E', 'D'):
            print('Argument 1 is not correct')
            print(help)
        elif sys.argv[2] not in ('C', 'M'):
            print('Argument 2 is not correct')
            print(help)
        elif type(int(sys.argv[3])) != int:
            print('Argument 3 is not correct')
            print(help)
        else:
            shift = int(sys.argv[3])
            if sys.argv[1] == 'E' and sys.argv[2] == 'C':
                output = caesar_encrypt(txt,shift)
            elif sys.argv[1] == 'D' and sys.argv[2] == 'C':
                output = caesar_decrypt(txt,shift)
            elif sys.argv[1] == 'E' and sys.argv[2] == 'M':
                output = encode_morse(txt)
            else:
                output = decode_morse(txt)

        output_file = open("output.txt", mode = "w")
        output_file.write(output)
        output_file.close



















