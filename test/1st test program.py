from test_question_class import Rectangle

def rectangle_program():
    while True:
        width=int(input("Enter the width of the rectangle: "))
        height=int(input("enter the height of the rectangle: "))
        if width=='0' or height=='0':
            print("Invalid")
            continue
        area = width * height
        print(f"width={width}\nheight={height} \narea= {area} ".format(width=width,height=height))
        cont = input("Do you want to continue? (y/n)")
        if cont == 'y':
            rectangle_program()
        else:
            break


my_rectangle= Rectangle()


if __name__ == "__main__":
    rectangle_program()