def simple_interest(p,r,t):
    return (p*r*t)/100

if __name__ == "__main__":
    p,r,t = map(int, input("Enter p,r,t in order: ").split())

    print(simple_interest(p,r,t))