def greet(name):
    print(f"Hello, {name}!")


def calculate_area(width,height):
 width  = int(width)
 height=int(height)
 area= width * height
 print(f"Area: {area} square units")
 return area


def main():
    user_name = input("Enter your name: ")
    greet(user_name)
    w = input("Enter width: ")
    h = input("Enter height: ")
    calculate_area(w,h)


if __name__ == "__main__":
    main()
