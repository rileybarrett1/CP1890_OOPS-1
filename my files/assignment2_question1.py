from dataclasses import dataclass


class person:
    @dataclass
    def __init__(self):
        self.firstname: str = ""
        self.lastname: str = ""
        self.email: str = ""

    def setfullname(self):
        self.firstname += " " + self.lastname

    def __instancecheck__(self, instance):
        return isinstance(self, person)


class customer(person):
    @dataclass
    def __init__(self):
        super().__init__()
        self.firstname: str = "frank"
        self.lastname: str = "wilson"
        self.email: str = "frank44@gmail.com"
        self.number: str = "m10293"

    def customerproperties(self):
        return f"{self.firstname} \n {self.lastname}\n {self.email} \n {self.number}"

class employee(person):
    @dataclass
    def __init__(self):
        super().__init__()
        self.firstname: str = "joel"
        self.lastname: str = "murach"
        self.email: str = "joel@murach.com"
        self.ssn: str = "123-45-6789"

    def employeeproperties(self):
        return f"firstname:{self.firstname} \n lastname:{self.lastname}\n email:{self.email} \n ssn:{self.ssn}"



while True:
    print("customer/employee data entry")
    user = input("customer or employee(c/e)")
    if user == "c":
        print("data entry")
        print(f"firstname: {}")