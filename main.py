from patterns.pyramid import number_pyramid
from patterns.inverted import inverted_pyramid
from patterns.floyd import floyd_triangle
from patterns.pascal import pascal_triangle

from utils.input_handler import get_positive_integer
from utils.display import show_menu

def main():
    while True:
        show_menu()
        choice = int(input("Enter choice: "))

        if choice == 5:
            break

        n = get_positive_integer()

        if choice == 1:
            number_pyramid(n)
        elif choice == 2:
            inverted_pyramid(n)
        elif choice == 3:
            floyd_triangle(n)
        elif choice == 4:
            pascal_triangle(n)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()



print("pyramid file loaded")