import sys
import os
import math

#encrpt 
class ADFGXdecrypt:
  def __init__(self,k=None, ct = None):
    self.key = self.remove_duplicates(k)
    self.keyword2 = self.remove_duplicates(k)
    self.cipher_text = ct
    self.alphabet = [chr(x+65) for x in range(26)]
    self.alphabetL = [chr(x+97) for x in range(26)]
    self.adfgx = ['A','D','F','G','X']
    self.polybius_matrix = []

    self.polybius = None
    self.Rpolybius = None
    self.AgainPolybius = None
    self.plain_text = ''
    self.polybius_builder = None
    self.look = None
    self.cipher_string = ''
    self.Real_plain_text = ''

    self.longCol = 0
    self.longRow = 0
    self.shortCol = 0
    self.shortRow = 0
    self.checkRow = 0
    self.checkCol = 0
  
  def remove_duplicates(self,key):
        """ Removes duplicate letters from a given key, since they
            will break the encryption.

            Example: 
                key = 'helloworldhowareyou'
                returns 'helowrdayu'

        """
        newkey = []             # create a list for letters
        for i in key:           # loop through key
            if not i in newkey: # skip duplicates
                newkey.append(i)
        
        # create a string by joining the newkey list as a string
        return ''.join(str(x) for x in newkey)
  
  def remove_nonalphabet(self):
    
    self.cipher_text = self.cipher_text.replace(' ', '')
    for i in self.cipher_text:
      if i not in self.alphabet:
        print("Error: there should only be letters from the english alphabet. Try again!")
      else:
        continue
    # print(self.cipher_text)
    return self.cipher_text
    # return 0
    

  
  def countRows_n_Cols(self):
    if self.cipher_text == None:
      self.remove_nonalphabet()

    self.longRow = math.ceil(len(self.cipher_text)/len(self.keyword2))
    self.longCol = len(self.cipher_text)%len(self.keyword2)
    self.shortRow = self.longRow - 1
    self.shortCol = len(self.keyword2) - self.longCol

    # print(len(self.cipher_text))
    # print(len(self.keyword2))
    # print(self.longCol)
    # print(self.longRow)
    # print(self.shortCol)
    # print(self.shortRow)
  
  def assign_R_n_C(self):
    if self.longRow == 0 or self.longCol == 0 or self.shortCol == 0 or self.shortRow == 0:
        self.countRows_and_Cols()
    
    self.polybius = {}

    for i in self.keyword2:
      self.polybius[i] = 0
    if self.longCol == 0:
      for i in range(len(self.keyword2)):
        self.polybius[self.keyword2[i]] = self.longRow

    else:
      for i in range(len(self.keyword2)):
        if i < self.longCol:
          self.polybius[self.keyword2[i]] = self.longRow
        elif i >= self.longCol:
          self.polybius[self.keyword2[i]] = self.shortRow
    
    return self.polybius
      

  def r_fractionating(self):
    if self.polybius == None:
      self.polybius = self.assign_R_n_C()
    
    self.Rpolybius = {}
    text = []
    count = 0

    if self.longCol == 0:
      for i in sorted(self.polybius.keys()):
        if self.polybius[i] == self.longRow:
          for j in range(self.longRow):
            text.append(self.cipher_text[j + count])
          self.Rpolybius[i] = text
          count += self.longRow
          # print(i,text)
          text = []
    else:
      for i in sorted(self.polybius.keys()):
        if self.polybius[i] == self.longRow:
          for j in range(self.longRow):
            text.append(self.cipher_text[j + count])
          self.Rpolybius[i] = text
          count += self.longRow
          # print(i,text)
          text = []
          # print(self.polybius[i], i, "long")
        elif self.polybius[i] == self.shortRow:
          for j in range(self.shortRow):
            text.append(self.cipher_text[j +count])
          self.Rpolybius[i] = text
          count += self.shortRow
          # print(i,text)
          text = []
        # print(self.polybius[i], i, "short")
    # print(self.Rpolybius)  
    return self.Rpolybius
  
  def keyword2_Polybius(self):
    if self.Rpolybius == None:
      self.Rpolybius = self.r_fractionating()
    
    self.AgainPolybius = {}
    for i in range(len(self.keyword2)):
      self.AgainPolybius[i] = []
    
    # print(self.AgainPolybius, "heree")
    randText = []
    for i in self.keyword2:
      for j in self.Rpolybius[i]:
        randText.append(j)
    # print(randText,"heyy")

    self.plain_text = self.columnar_transposition_matrix(randText)
    
    return self.plain_text

  def columnar_transposition_matrix(self,randText):
      # print("transpose")
      randT = randText
      # print(randT,"rand")
      rows = self.longRow
      cols = self.longCol
      # print (rows,cols, " ", Srow, Scol)
      if self.longCol != 0:
        # print("not in 0")
        m=[]
        for i in range(cols):
          col = []
          for j in range(rows):
            # print(randT[0])
            col.append(randT[0])
            randT.remove(randT[0])
          m.append(col)
        # print(m)
        # print(randT)

        Srow = self.shortRow
        Scol = self.shortCol
        P = []
        for k in range(Scol):
          Scol = []
          for l in range(Srow):
            # print(randT[0])
            Scol.append(randT[0])
            # print(Scol)
            randT.remove(randT[0])
          P.append(Scol)
        # print(P)
        pt = ''
        remin=0
        # pt+=P[0][0]
        # print(pt)
        for i in range(self.shortRow):
          for j in range(self.longCol):
            pt+=m[j][i]
          for j in range(self.shortCol):
            pt+=P[j][i]
        remin = i + 1
        # print(remin)

        for i in range(remin,rows):
          for j in range(self.longCol):
            pt+=m[j][i]

      elif self.longCol == 0:
        y=[]
        # print(self.shortCol,self.longRow)
        for i in range(self.shortCol):
          co = []
          for j in range(self.longRow):
            co.append(randT[0])
            randT.remove(randT[0])
          y.append(co)
        pt = ''
        # print(y)
        remin=0
        # pt+=P[0][0]
        for i in range(self.longRow):
          for j in range(self.shortCol):
            pt+=y[j][i]
        remin = i + 1

        for i in range(remin,rows):
          for j in range(self.shortCol):
            pt+=y[j][i]

      # print(m[0][0],m[1][0],P[0][0], P[1][0])

      return pt

  def keyword(self,k=None):
    self.key = self.remove_duplicates(k)

    return self.key

  def build_polybius_string(self,key=None):
          """Builds a string consisting of a keyword + the remaining
            letters of the alphabet. 
            Example:
                  key = 'superbatzy'
                  polybius = 'superbatzycdfghiklmnoqvwx'
          """
          # no key passed in, used one from constructor
          if key != None:
              self.key = self.remove_duplicates(key)

          # NO key!
          if not self.key:
              print("Error: There is NO key defined to assist with building of the matrix")
              sys.exit(0)

          # key exists ... continue
          self.keylen = len(self.key)

          # prime polybius_string variable with key
          self.polybius_builder = self.key

          #loops through the alphabet (except 'j')
          for l in self.alphabetL:
              if l == 'j':        # no j needed!
                  continue
              if not l in self.key:    # if letter not in key, add it
                  self.polybius_builder += l
          return self.polybius_builder

  def build_polybius_lookup(self,key=None):
    if key != None:
      self.key = self.remove_duplicates(key)

          # NO key!
    if not self.key:
      print("Error: There is NO key defined to assist with building of the matrix")
      sys.exit(0)
    
    if self.polybius_builder == None:
      self.build_polybius_string()
    
    self.lookup = {} 
    for l in self.polybius:
      self.lookup[l] = ''

    row = 0 
    col = 0

          # loop through the polybius 1D string and get the 2 letter pairs
          # needed to do the initial encryption
    for row in range(5):
      for col in range(5):
        i = (5 * row) + col
        self.lookup[self.polybius[i]] = self.adfgx[row]+self.adfgx[col]

    return self.lookup

  def identify_PT(self):
    # i = 0
    if self.plain_text == None:
      self.plain_text = self.keyword2_Polybius()

    cipher_test_text = ''
    # print(len(self.plain_text))
    j = 0
    for i in range(len(self.plain_text)):
      if j%2 == 0:
        cipher_test_text+= self.plain_text[i]
      elif j%2 == 1:
        cipher_test_text+= self.plain_text[i]
        cipher_test_text+= " "
      j+=1
    # print(self.cipher_string)
    self.cipher_string = cipher_test_text
    return self.cipher_string
  
  def lookRC_to_PS(self):
    if self.cipher_string == '':
      self.identify_PT()

    final_pt = ''
    cip_key = self.cipher_string
    # print(cip_key)
    j=0
    for i in range(len(cip_key)):
      if cip_key[i] == " ":
        continue
      else:
        if j%2 == 0:
          let1 = cip_key[i]
        elif j%2 == 1:
          let2 = cip_key[i]
          final_pt+=self.lookup_chart(let1,let2)
        j+=1
      self.Real_plain_text = final_pt
    # print(self.Real_plain_text)
    return self.Real_plain_text
    
  def identify_ADFGX(self,Let):
    if Let == 'A' :
      return 0;
    elif Let == 'D':
      return 1;
    elif Let == 'F':
      return 2;
    elif Let == 'G':
      return 3;
    elif Let == 'X':
      return 4;

  def lookup_chart(self,R,C):
    self.checkRow = self.identify_ADFGX(R)
    self.checkCol = self.identify_ADFGX(C)
    # print(self.checkRow,self.checkCol)
    # print(self.polybius_matrix)
    t = self.polybius_matrix[self.checkRow][self.checkCol]
    # print(t)
    return t

  def p_matrix(self):
    if self.polybius_builder == None:
      self.build_polybius_string()

    for r in range(5):
      col = []
      for c in range(5):
        i = (5 * r) + c
        # print(self.polybius_builder[i])
        col.append(self.polybius_builder[i])
      self.polybius_matrix.append(col)
    # print(self.polybius_matrix)
    return self.polybius_matrix

  def decrypt_text(self,text, keyw1, keyw2):
      keyWord2 = keyw2
      cipherText = text
      S = ADFGXdecrypt(keyWord2, cipherText)
      S.remove_nonalphabet()
      S.countRows_n_Cols()
      S.assign_R_n_C()
      S.r_fractionating()
      S.keyword2_Polybius()
      S.keyword(keyw1)
      S.identify_PT()
      S.p_matrix()
      return S.lookRC_to_PS()

ALPHABET = [chr(x+97) for x in range(26)]

class ADFGXencrypt:
    def __init__(self,k=None):
        #key with distinct letters
        self.key = self.remove_duplicates(k)
        self.key2 = ''
        #elements of the alphabet
        self.alphabet = [chr(x+97) for x in range(26)]
        #the ROW/COL header
        self.adfgx = ['A','D','F','G','X']
        #length of keyword
        self.keylen = 0
        #length of keyword 2
        self.keylen2 = 0

        #rows and cols for 
        self.longRow = 0
        self.longCol = 0
        self.shortRow = 0
        self.shortCol = 0

        #keyword1 exists then grab length of keyword1
        if self.key:
            self.keylen = len(self.key)
        if self.key2:
            self.keylen2 = len(self.key2)

        self.polybius = None
        self.lookup = None
        self.polybius_2 = None
        self.cipher1 = None
        self.plain = None
        self.decipherText = None
    
    #function to avoid duplicates in keyword
    def remove_duplicates(self,key):
        newkey = []             # create a list for letters
        for i in key:           # loop through key
            if not i in newkey: # skip duplicates
                newkey.append(i)
        
        # create a string by joining the newkey list as a string
        return ''.join(str(x) for x in newkey)
       
    #creates string needed for the Polybius Square
    #avoids the letter j and joins the keyword to the rest of the alphabet (without duplicates)
    def build_polybius_string(self,key=None):
        # no key passed in, used one from constructor
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # key exists ... continue
        self.keylen = len(self.key)

        # prime polybius_string variable with key
        self.polybius = self.key

        #loops through the alphabet (except 'j')
        for l in self.alphabet:
            if l == 'j':        # no j needed!
                continue
            if not l in self.key:    # if letter not in key, add it
                self.polybius += l
        return self.polybius

    #creating dictionary for the alphabet 
    def build_polybius_lookup(self,key=None):
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        # init our dictionary
        self.lookup = {}            # dict as our adfgx reverse lookup
        for l in self.polybius:     # loop through the 1D matrix we created
            self.lookup[l] = ''     # init keys in the dictionary

        row = 0 
        col = 0

        # loop through the polybius 1D string and get the 2 letter pairs
        # needed to do the initial encryption
        for row in range(5):
            for col in range(5):
                i = (5 * row) + col
                self.lookup[self.polybius[i]] = self.adfgx[row]+self.adfgx[col]

        return self.lookup
    
    def filter_plain_text(self,plain_text):
      plain = ''
      for i in plain_text:
        if i not in self.alphabet:
          continue
        else:
          plain += i
      # print(plain,"filter_plain_text")
      return plain.lower()

    def plain_text_identifier(self, plain_text):
      self.plain = self.filter_plain_text(plain_text)
      self.cipher1=''

      if(self.lookup == None):
        self.lookup = self.build_polybius_lookup()

      # num = 0
      for i in self.plain:
        self.cipher1 += self.lookup[i]
      # for x in range(len(self.cipher1)): 
      #   print(self.cipher1[x])
      return self.cipher1
    
    def keyword_2(self, k = None):
      self.key2 = self.remove_duplicates(k)
      self.keylen2 = len(self.key2)

    def Rows_and_Cols(self):
      if not self.key2:
        print("Error: There is NO keyword 2 defined to assist with building of the matrix")
        sys.exit(0)

      self.longRow = math.ceil(len(self.cipher1)/len(self.key2))
      self.longCol = len(self.cipher1)%len(self.key2)
      self.shortRow = self.longRow - 1
      self.shortCol = self.keylen2 - self.longCol
      # print(self.longRow)
      # print(self.longCol)
      # print(self.shortRow)
      # print(self.shortCol)

    def make_k2_poly_squ(self): 
      if not self.key2:
        print("Error: There is NO keyword 2 defined to assist with building of the matrix")
        sys.exit(0)

      if self.longRow == 0 or self.longCol == 0 or self.shortCol == 0 or self.shortRow == 0:
        self.Rows_and_Cols()
      
      self.polybius_2 = {}
      
      textlist = []
      
      for i in self.key2:
        self.polybius_2[i] = textlist
      if self.longCol == 0:
        for i in range(self.keylen2):
            for j in range(self.longRow):
              textlist.append(self.cipher1[(j*self.keylen2 + i)])
            self.polybius_2[self.key2[i]] = textlist
            textlist = []  
      else:
        for i in range(self.keylen2):
          if i < self.longCol:
            for j in range(self.longRow):
              textlist.append(self.cipher1[(j*self.keylen2 + i)])
            self.polybius_2[self.key2[i]] = textlist
            textlist = []
          elif i >= self.longCol:
            for j in range(self.shortRow):
              textlist.append(self.cipher1[(j*self.keylen2 + i)])
            self.polybius_2[self.key2[i]] = textlist
            textlist = []
      return self.polybius_2
    
    def fractionating(self):
      self.decipherText = ''
      if self.polybius_2 == None:
        self.polybius_2 = self.make_k2_poly_squ()
      
      # print(self.polybius_2)
      # print("here")
      printtext = ''
      for i in sorted(self.polybius_2.keys()):
        # print(self.polybius_2[i])
        printtext = self.polybius_2[i]
        
        for ii in range(len(printtext)):
          self.decipherText += printtext[ii]
      # print(printtext,"k")  
      # print(self.decipherText,"h")
      return self.decipherText
        
    def print_decipher(self):
      cipher_txt =''
      if self.decipherText == None:
        self.decipherText = self.fractionating()
      
      j = 0
      for i in self.decipherText:
        if j%2 == 0:
          cipher_txt += i
        elif j%2 == 1:
          cipher_txt += i
          cipher_txt += " "
        j+=1
      # print(self.decipherText)
      return cipher_txt

    def encrypt_text(self,text, keyw1, keyw2):
      self.plain_text_identifier(text)
      self.keyword_2(keyw2)
      return self.print_decipher()

def ADFGX_cipher_decrypt(**kwargs):
    input_file = kwargs.get('input',None)
    output_file = kwargs.get('output',None)
    key = kwargs.get('key',None)
    key2 = kwargs.get('key2',None)

    # should test if file exists
    with open(input_file) as f:
        plaintext = f.read()

    B = ADFGXdecrypt(key)
    ciphertext = ''
    ciphertext = B.decrypt_text(plaintext, key, key2)

    with open(output_file,'w') as f:
        f.write(ciphertext)

def ADFGX_cipher_encrypt(**kwargs):
    input_file = kwargs.get('input',None)
    output_file = kwargs.get('output',None)
    key = kwargs.get('key',None)
    key2 = kwargs.get('key2',None)

    # should test if file exists
    with open(input_file) as f:
        plaintext = f.read()

    B = ADFGXencrypt(key)
    ciphertext = ''
    ciphertext = B.encrypt_text(plaintext, key, key2)

    with open(output_file,'w') as f:
        f.write(ciphertext)

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs


def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename] [key=string] [key2=string] [op=encrypt/decrypt]")
    # print(f"Example:\n\t python {name} input=input_file.txt output=output_file.txt key=machine op=encrypt\n")
    sys.exit()

if __name__=='__main__':
    required_params = 5 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    operation = params.get('op',None)
    infile = params.get('input',None)
    outfile = params.get('output',None)
    key = params.get('key',None)
    key2 = params.get('key2',None)

    if not operation and not infile and not outfile and not key:
        usage()

    if operation.lower() == 'encrypt':
        ADFGX_cipher_encrypt(**params)
    elif operation.lower() == 'decrypt':
        ADFGX_cipher_decrypt(**params)
    else:
        usage()
