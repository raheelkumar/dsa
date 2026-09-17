def sum_two_num(a,b):
    return a + b

if __name__ == "__main__":
    a,b = map(int, input("Enter two numbers: ").split())

    print(sum_two_num(a,b))