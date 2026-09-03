class Library:
    def __init__(self):
        self.Book = {}
        self.Student = {}
        self.Empolyee = {}

    def Add_book(self, obj):
        if obj.b_id not in self.Book:
            self.Book[obj.b_id] = obj
            print("Book added successfully")
        else:
            print("ID already exists")

    def View_books(self):
        if len(self.Book) != 0:
            for i in self.Book.values():
                print(i.b_id, i.name, i.author, i.copies, i.remaining)
                print()
        else:
            print("Books are not available")

    def Add_std(self, std):
        if std.s_id not in self.Student:
            self.Student[std.s_id] = std
            print("Student successfully added")
        else:
            print("Student ID already exists")

    def View_std(self):
        if len(self.Student) != 0:
            for i in self.Student.values():
                print(i.s_id, i.name, i.email)
        else:
            print("Students are not available")

    def Add_emp(self, emp):
        if emp.e_id in self.Empolyee:
            print(f"{emp.name} already exists")
        else:
            self.Empolyee[emp.e_id] = emp
            print(f"{emp.name} created successfully")

    def View_emp(self):
        if len(self.Empolyee) != 0:
            for i in self.Empolyee.values():
                print(i.e_id, i.name)
        else:
            print("Employees are not available")

    def Login(self, e_id):
        if e_id not in self.Empolyee:
            print("Employee does not exist")
        else:
            employee = self.Empolyee[e_id]
            employee.Menu(self)


class Book:
    def __init__(self, b_id, name, author, copies):
        self.b_id = b_id
        self.name = name
        self.author = author
        self.copies = copies
        self.remaining = copies

    def availble(self):
        if self.remaining > 0:
            self.remaining -= 1
            return True
        return False


class Student:
    def __init__(self, s_id, name, email):
        self.s_id = s_id
        self.name = name
        self.email = email
        self.having = []


class Empolyee:
    def __init__(self, e_id, name):
        self.e_id = e_id
        self.name = name

    def Menu(self, l):
        while True:
            print("\n1. Add book")
            print("2. View book")
            print("3. Add Student")
            print("4. View Student")
            print("5. Add Employee")
            print("6. View Employee")
            print("7. Allocate book")
            print("8. Logout")

            n = int(input("Enter option: "))

            if n == 1:
                book_id = int(input("Book ID: "))
                book_name = input("Book Name: ")
                book_author = input("Book Author: ")
                book_copies = int(input("Book Copies: "))

                book_obj = Book(
                    book_id,
                    book_name,
                    book_author,
                    book_copies
                )

                l.Add_book(book_obj)

            elif n == 2:
                l.View_books()

            elif n == 3:
                student_id = int(input("Student ID: "))
                student_name = input("Student Name: ")
                student_email = input("Student Email: ")

                student_obj = Student(
                    student_id,
                    student_name,
                    student_email
                )

                l.Add_std(student_obj)

            elif n == 4:
                l.View_std()

            elif n == 5:
                emp_id = int(input("Employee ID: "))
                emp_name = input("Employee Name: ")

                emp = Empolyee(emp_id, emp_name)

                l.Add_emp(emp)

            elif n == 6:
                l.View_emp()

            elif n == 7:
                b_id = int(input("Book ID: "))
                s_id = int(input("Student ID: "))

                self.allocate_book(l, b_id, s_id)

            elif n == 8:
                print("Logged out successfully")
                break

            else:
                print("Invalid option")

    def allocate_book(self, l, b_id, s_id):

        if b_id not in l.Book:
            print("Book not available")
            return

        if s_id not in l.Student:
            print("Student does not exist")
            return

        book = l.Book[b_id]
        student = l.Student[s_id]

        if book.availble():
            student.having.append(b_id)
            print("Successfully allocated to student")
        else:
            print("Books not available")


# Library object
l = Library()


# Main program
while True:

    print("\n1. Create employee")
    print("2. Login")
    print("3. Exit")

    n = int(input("Enter option: "))

    if n == 1:
        e_id = int(input("Employee ID: "))
        name = input("Employee Name: ")

        emp = Empolyee(e_id, name)

        l.Add_emp(emp)

    elif n == 2:
        e_id = int(input("Employee ID: "))
        l.Login(e_id)

    elif n == 3:
        print("Program ended")
        break

    else:
        print("Invalid option")