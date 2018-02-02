"""sentence = str(input('Give a sentence of words: '))

words = sentence.split()

sentLen = int(len(words))

if((sentLen%2)==0):
    print('Middle word(s): ',words[int(sentLen/2)-1],words[int(sentLen/2)])
else:
    print('Middle word(s): ', words[(int(sentLen / 2))])
"""    
    
    
query = input("Enter a sentence :")

def find_reverse():
    a = query[::-1] #reversing the given string and storing in different variable
    b = a.split() #spliting the string
    c = []
    x = len(b) - 1  #reducing the length as from back it starts from -1
    while x >= 0:
        c.append(b[x])
        x = x - 1
    out = " ".join(c)
    print('\nSentence with reverse operation is :',out)

def find_middle():
  z = query.split()
  length = int(len(z))
  
  if length%2 is 0:
    print('\nMiddle word is : ',z[int(length/2)-1],z[int(length/2)])
  else:
    print('\n Middle word is :',z[int(length/2)])
  

def find_longest():
        print('\nLongest word is:', max(query.split(), key=len))


find_middle()
find_longest()
find_reverse()

