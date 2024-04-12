from datetime import datetime

from date_test_class import countdown

def program():
    user_input=input("enter target datetime (yyyy-m-d:): ")
    user_input=datetime.strptime("%y-%m-%d",user_input)
    print(user_input)









if __name__ == '__main__':
    program()