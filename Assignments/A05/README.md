# Assignment 5 - Vigenere Cracking

### Arshia Clare
### Description:

You will be given 1 or more encrypted files. You know the files were encrypted using the Vigenère method. You also know that the key used is an english dictionary word with a length 2-16 inclusive.

Write a python program that will 1) discover the size of that dictionary word (keylength) and then determine which word was used to encrypt your file(s).

To find the keylength you can use the Index of Coincidence (I.C.)

Where c=26,
ni is the frequency of each letter,
and N is the length of the text.

The output prints the key-length, keyword that was identified, 50 words of the message after decryption.

Run the program:
python3 break_vig.py input=encrypted


### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   |[.replit](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/.replit)|.replit (to run the program|
|   2   |[break_vig.py](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/break_vig.py)| main program that performs the task to find the key length, keyword, and decrypted message|
|   3   |[encrypted1.txt](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/encrypted1.txt)|input 1|
|   4   |[decrypted1.txt](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/decrypted1.txt)|output 1 with the keyword "abolitionising"|
|   5   |[encrypted2.txt](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/encrypted2.txt)|input 2|
|   6   |[decrypted2.txt](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/decrypted2.txt)| output 2 with the keyword "aahed"|
|   7   |[words.txt](https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A05/words.txt)|the list of words |

# Sources
https://cryptii.com/pipes/vigenere-cipher
https://www.w3schools.com/python/python_dictionaries.asp
https://www.w3schools.com/python/python_lists.asp
http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/
http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/
Methods for dictionary, list, etc.
Codes provided by Dr.Griffin

