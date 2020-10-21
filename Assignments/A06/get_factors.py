import sys
import os
import math

class Prime:
  def __init__(self):
    self.testnum = 0
    self.sq_root = 0
    self.primeList = []
    self.isFactor = False
    self.Factors = []
  
  def squareroot(self):
    self.sq_root = math.ceil(math.sqrt(self.testnum))
    return self.sq_root
  
  def createPrimeList(self):
    if self.sq_root == 0:
      self.sq_root = math.ceil(self.squareroot())
    for i in range(2, self.testnum):
      self.primeList.append(i)
    return self.primeList

  def findPrimeList(self):
    if self.primeList == []:
      self.primeList = self.createPrimeList()
    j = 0
    i = 1
    while(j < self.sq_root):
      while(i < len(self.primeList)):
        if(self.primeList[i]%self.primeList[j]==0):
          self.primeList.remove(self.primeList[i])
        else: 
          i+=1
      j+=1
      i=j+1
    return self.primeList
  
  def factor(self):
    if self.primeList == []:
      self.primeList = self.findPrimeList()
    num = self.testnum
    for i in self.primeList:
      while(num%i == 0):
        num=num/i
        self.Factors.append(i)
    return self.Factors
  
  def isitPrime(self):
    if len(self.Factors) == 0:
      self.isFactor = False
    else:
      self.isFactor = True
    return self.isFactor

  def printPRIME(self,num = 0):
    self.testnum = num
    self.sq_root = 0
    self.primeList =[]
    self.createPrimeList()
    self.findPrimeList()
    self.Factors = []
    self.factor()
    self.isitPrime()
    return self.isFactor

def prime_read(**kwargs):
    input_file = kwargs.get('input',None)
    output_file = kwargs.get('output',None)
    num = []
    A = Prime()
    isBool = False
    # should test if file exists
    with open(input_file, "r") as f:
      num = (f.readlines())
    for i in range(len(num)): 
      num[i] = int(num[i].strip())

    with open(output_file,'w') as f:
      f.write("Name: Arshia Clare")
      for i in range(len(num)):
        isBool = A.printPRIME(num[i])
        if isBool == False:
          f.write("Number " + str(i+1) + ": " + str(num[i]) + " - Prime\n")
        else:
          f.write("Number " + str(i+1) + ": " + str(num[i]) + " - Factors: ")
          numlist = A.Factors
          for j in range(len(numlist)):
            f.write(str(numlist[j] ))
            if j != len(numlist)-1:
              f.write(" * ")
          f.write('\n')

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
    print(f"Usage: python {name} [input=string filename] [output=string filename]")
    print(f"Example:\n\t python {name} input=input_file.txt output=output_file.txt \n")
    sys.exit()

if __name__=='__main__':
  num = []
  required_params = 2
  _,params = mykwargs(sys.argv[1:])
  if len(params) < required_params:
    usage()
  infile = params.get('input',None)
  outfile = params.get('output',None)
  
  if not infile and not outfile:
    usage()
  
  prime_read(**params)
