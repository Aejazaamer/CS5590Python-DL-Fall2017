class Person:                                   # class Person
  
    def __init__(self,name,emailaddr):          # init constructor
        self.name = name
        self.emailaddr = emailaddr
    def display(self):                          # self used in each method of a class
        print("Name: ", self.name)
        print("email: ", self.emailaddr)

class Student(Person):                          # class student is inheriting class Person
    Count = 0
    def __init__(self,name,email,id_number):    # init constructor
        Person.__init__(self,name,email)
        self.id_number= id_number
        Student.Count +=1
   
    def display(self):
        print("\nStudent:")
        Person.display(self)
        print("Student Id: ",self.id_number)

class Librarian(Person):
  
    def __init__(self,name,email,employee_id):   # init constructor
        super().__init__(name,email)             # super call
        self.employee_id = employee_id
    def __display(self):                         # private data member 
        print("Librarian:")
        Person.display(self)
        print("Employee Id: ",self.employee_id)

class Book():
    def __init__(self,book_name,author,book_id): # init constructor
        self.book_name = book_name
        self.author = author
        self.book_id = book_id
    def display(self):
        print("\nBook available in library:")
        print("book_name: ", self.book_name)
        print("Author_name: ", self.author)
        print("Book_ID: ", self.book_id)

class lend_Book(Student,Book):                    # multiple inheritance used here
    def __init__(self,name,email,student_id,book_name,author,book_id):  # init constructor
        Student.__init__(self,name,email,student_id)
        Book.__init__(self,book_name,author,book_id)
        
    def display(self,days):
        self.days = days
        print("\nRented Book :")
        Student.display(self)
        print('rented book is :',self.book_name)
        print('Return book by :',self.days, 'days')

lib = Librarian('messi','messi@gmail.com',100)  # instance of class Librarian
lib._Librarian__display()                       # Accessing private data member using an instance
stu1 = Student('ronaldo','cr7@icloud.com',123)  # instance of class Student
stu1.display()
stu2 = Student('bale','bale@yahoo.com',789)     # instance of class student
stu2.display()
print("\nTotal Number of Students:", Student.Count)
b = Book('harry potter','J K rowling',5448569)  # instance of class Book
b.display()
l = lend_Book('bale','bale@yahoo.com',456,'harry potter','J K rowling',5448569)
l.display(7)        # instance of class lend_book used to display rented book name along with student details  
