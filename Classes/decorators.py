def f1():
     print("called f1")


# def f2(f):
#     f()
#
# f2(f1)

def f1(func):
    def wrapper():
        print("started")
        func()
        print("finished")
    return wrapper
@f1
def f():
    print("Hello")

# print(f1(f))
#  f1(f)()
# x = f1(f)
# x()
f("lets dance")

@timer
def run():
    time.sleep(2)

run()