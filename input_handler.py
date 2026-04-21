def get_positive_integer():
    while True:
        try:
            n = int(input("Enter number of rows: "))
            if n > 0:
                return n
            else:
                print("Enter positive number!")
        except ValueError:
            print("Invalid input!")