from product_viewer_program_cls import ProductViewer,Prices

def main():
    print("Product viewer program")
    while True:
        viewer = ProductViewer()
        prices = Prices()
        viewer.display_products()
        product_number = int(input("Enter product number: "))
        if product_number == 1:
            print(f"name: {viewer.products(0)}")
        if product_number == 2:
            print(f"name:{viewer.products(1)}")
        if product_number == 3:
            print(f"name:{viewer.products(2)}")








if __name__ == "__main__":
    main()