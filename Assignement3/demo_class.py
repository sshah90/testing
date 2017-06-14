# this script is for answers for que 1,2,4,7

# class
class Employee:


    # constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



    def getString(self):
        self.name=input("Give me any string :- ")


    def printString(self):
        print("Given string in upeer case :- ",self.name.upper())



# inheritance understanding
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# object understanding
dev_1 = Developer('Smit', 'Shah', 50000, 'Python')
dev_2 = Developer('Hani', 'Patel', 60000,'Java')
emp_1=Employee('Nix','Patel',25888)
print(emp_1.email)
print(dev_1.fullname())
dev_1.getString()
dev_1.printString()