Clist=[{'Name':'aamer','Number':'9554520210','email':'aa@gmail.com'},{'Name':'zaheer','Number':'9578975800','email':'zz@gmail.com'}]

print('Contacts List')

while True:
  print('\nSelect your option:')
  print('1. show contact by name')
  print('2. show contact by number')
  print('3. change contact by name')
  print('4. Exit')
  
  inp1 = int(input('\nEnter one of the option:'))
  
  if inp1 == 1:
    print('contacts by name :')
    for p in Clist:
        i = 0
        while(i<1):
              z =  p['Name']
              print(z)
              i += 1
    break
      
  elif inp1 == 2:
    print('contacts by number :')
    for n in Clist:
      j = 0
      while(j<1):
        a = n['Number']
        print(a)
        j += 1
    break
    
      
  elif inp1 == 3:
    print(Clist)
    inp2 = input('\nEnter contact name to edit number:')
    inp3 = input('\nEnter the new number:')
    print(inp2)
    for a in Clist:
      if a['Name'] in inp2:
        a['Number'] = inp3
        print(Clist)
    break
      
   
   
   
  elif inp1 == 4:
     print('Exit succes')
     break
   
  else:
    print('Wrong input')
    continue
