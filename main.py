def main():

    try: 
        product_list = []
        infile = open("theProductList.txt", "r")
        line = infile.readline()
        while line:
            product_list.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    
    except:
        print("The <product_list.txt>  file not found")
        print("Starting a new Product List")
        product_list = []

    choice = 0
    while choice !=4:
        print("*****e-commerce manager****")
        print("1) Add a Product")
        print("2) See the Product")
        print("3) Display Product")
        print("4) Quit")
        choice = int(input("Enter a Choice Number: "))

        if choice == 1 :
            print(" Add a New Product")
            name_product=input(" Enter name of product: ")
            category_product=input(" Enter category of product: ")
            price_product=input(" Enter amt of product: ")
            if price_product>10000:
                discountprice = price_product-500
                print(discountprice)
            else:
                print(price_product,"No discount because amount is not greater than 10000")
            product_list.append([name_product, category_product, price_product])

        elif choice == 2:
            print("See the Product details")
            keyword = input("Enter a Search Term : ")
            for product in product_list:
                if keyword in product:
                    print(product)

        
        elif choice == 3:
            print("Display all the Products: ")
            for i in range(len(product_list)):
                print(product_list[i])

        
        elif choice == 4:
            print(" Quiting the program ")

    print(" Program Stopped !!!!!")

    #Saving to external file
    outfile = open("theProductList.txt", "w")
    for product in product_list:
        outfile.write(",".join(product)+ "\n")
    outfile.close()




if __name__ == "__main__":
    main()