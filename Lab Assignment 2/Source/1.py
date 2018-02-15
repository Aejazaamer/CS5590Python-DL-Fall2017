print('Welcome to UMKC book shop!\n')

dict1 = {'python':50,'web':30,'c':20,'java':40}
list1 = list(dict1.values())
list2 = []
list3 = []

print('give me a min and maximum range for the cost of book:')
inp = int(input('min cost :'))
inp1 = int(input('max cost:'))


for i in range(inp,inp1+1):
  list2.append(i)
  
for name, item in dict1.items():
  if item in list2:
    list3.append(name)
  
    
print('you can purchase books:',list3)
 

  









