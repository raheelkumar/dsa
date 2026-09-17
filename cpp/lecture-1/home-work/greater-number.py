def greater_number(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "Equal"

if __name__ == "__main__":
    a,b = map(int, input("Enter two numbers: ").split())

    print(greater_number(a,b))