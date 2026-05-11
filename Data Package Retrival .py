while True:   
    print("MAIN MENU\n1. All Time Data Pack\n2. Recurring Pack\n3. SMS Pack\n4. Unlimited Facebook/YouTube Pack\n5. Exit")
    choice=int(input("Enter a choice: "))
    if choice==1:
        print("ALL TIME  DATA PACK\n1. 1GB @ Rs 30 - 1 Day\n2. 4GB @ Rs 99 - 1 Day\n3. 5GB @ 109 - 7 Days\n4. 12GB @ 199")
        pack=int(input("Enter a pack: "))
        if pack==1:
            print("Selected Pack: 1GB @ Rs 30 - 1 Day")
            print("Return TO Main Menu")
        elif pack==2:
            print("Selected Pack: 4GB @ Rs 99 - 1 Day")
            print("Return TO Main Menu")
        elif pack==3:
            print("Selected Pack: 5GB @ 109 - 7 Days")
            print("Return TO Main Menu")
        elif pack==4:
            print("Selected Pack: 12GB @ 199")
            print("Return TO Main Menu")
        else:
            print("Invalid")
    elif choice==2:
        print("RECURRING PACK\n1. 700MB/Day @ Rs 299 - 28 Day\n2. 1.2GB/Day @ Rs 599 - 28 Day")
        pack=int(input("Enter a pack: "))
        if pack==1:
            print("Selected Pack: 700MB/Day @ Rs 299 - 28 Day")
            print("Return TO Main Menu")
        elif pack==2:
            print("Selected Pack: 1.2GB/Day @ Rs 599 - 28 Day")
            print("Return TO Main Menu")
        else:
            print("Invalid")
    elif choice==3:
        print("SMS PACK\n1. 200 SMS @ Rs 35 - 1 Day\n2. 200 SMS @ Rs 60 - 7 Days\n3. 500 SMS @ Rs 150 - 28 Days")
        pack=int(input("Enter a pack: "))
        if pack==1:
            print("Selected Pack: 1. 200 SMS @ Rs 35 - 1 Day")
            print("Return TO Main Menu")
        elif pack==2:
            print("Selected Pack: 2. 200 SMS @ Rs 60 - 7 Days")
            print("Return TO Main Menu")
        elif pack==3:
            print("Selected Pack: 3. 500 SMS @ Rs 150 - 28 Days")
            print("Return TO Main Menu")
        else:
            print("Invalid")