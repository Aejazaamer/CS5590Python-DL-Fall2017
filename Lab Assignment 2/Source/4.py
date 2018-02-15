import numpy as np                #  import numpy 

Z = np.random.randint(0,21,15)    # creating a random integers in the range 0 - 20
print(Z)

print('\nRepeated item in the list is:',np.bincount(Z).argmax())