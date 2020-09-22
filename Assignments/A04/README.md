## Assignment 4 - ADFGX
### Arshia Clare
#### Description

The ADFGX cipher was a field cipher used by the German Army during World War I. It is closely related to the ADFGVX cipher. ADFGX is a fractionating transposition cipher which combined a modified Polybius square with a single columnar transposition. The cipher is named after the five possible letters used in the ciphertext: A, D, F, G and X. These letters were chosen deliberately because they sound very different from each other when transmitted via morse code. The intention was to reduce the possibility of operator error.
Build the polybius square, The polybius square works by locating the letter in the matrix, then pulling out the letter at the beginning of the row, and the letter at the top of the column.
Ok, we know how to build our polybius square and use it to encode a word. But, were just getting started! There are a couple of steps that are involved in this whole ADFGX world-wind tour of encryption. So lets do this!
We have already chosen keyword1 to build the square with.
We built the square.
We can start the encryption of a message with said polybius square (essentially doubling the text length).
For the next steps, let us assume we are going to encrypt a single word: discombobulate (meaning: to confuse someone). 
Choose yet another keyword (that does not have duplicate letters) (we'll call this keyword2).
Write your encoded message below keyword2 as if each letter of keyword2 is a column header.
Add the message to the matrix in a row-wise fashion.
The next step is to perform a columnar transposition. Sort the code word alphabetically, moving the columns as you go. Note that the letter pairs that make up each letter get split apart during this step, this is called fractionating.
Read the final ciphertext off in columns to get the message that will be sent (I kept the spaces in for readability):

Decrypting:
To decrypt the message sent using our ADFGX cipher, we "simply" (LOL) reverse the steps. Of course the receiver needs keyword1 and keyword2 so they can build the modified Polybius square. But also piece back together the message that they received by reversing the fractionating process by:

Calculating the number of rows in the matrix based on length of keyword2.
Figuring out the number of short columns.
Assigning short columns to proper letters.
Alphabetizing the keyword2.
Read message back out from

#### Files
|   name   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|adfgx.py| https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A04/adfgx.py | the main program that contains the classes: ADFGXdecrypt, ADFGXencrpt |
|.replit|https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A04/.replit| running the program |
|   name   | Folder                       | Description                                           |
|input1|https://github.com/ArshiaClare/4663-Cryptography-Clare/tree/master/Assignments/A04/input1 | input folder contains input and output (encryption) |
|   name   | File                       | Description                                                |
|inputTextEnc.txt | https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A04/input1/inputTextEnc | just a random string |
|encrypted.txt | https://github.com/ArshiaClare/4663-Cryptography-Clare/blob/master/Assignments/A04/input1/encrypted.txt | the output|



#### Instructions
- This project was complied using python
- You need specify input, output, operation (decrypt or encrypt). keyword 1 to create the polybius square, keyword 2

#### Sources
https://github.com/rugbyprof/4663-Cryptography/tree/master/Assignments/A04 
Starter code
