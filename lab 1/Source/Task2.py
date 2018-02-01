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


def find_longest():
        print('\nLongest word is:', max(query.split(), key=len))


find_reverse()
find_middle()
find_longest()