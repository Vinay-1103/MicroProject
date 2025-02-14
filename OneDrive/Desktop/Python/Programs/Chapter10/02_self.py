class Employee:
    language = "Python"
    salary =100000

    def getInfo(self):
        print(f"The language is {self.language},The salary is {self.salary}")
    
    def greet(self):
        print("Hello Welcome")

aa = Employee()
aa.greet()
aa.getInfo()