class Employee:
    language = "python"
    salary = 120000

    def __init__(self,name,language,salary):
        self.name = name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getInfo(self):
        print(f"The salary {self.salary},The language {self.language}")

aa=Employee("Vinay",160000,"js")
print(aa.name,aa.language,aa.salary)

aa.getInfo()