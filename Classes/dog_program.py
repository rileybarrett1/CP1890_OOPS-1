# class Dog:
#
#     # class attribute
#     attr1 = "mammal"
#
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
#
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
#
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))
#
# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()

