def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print_items(n)