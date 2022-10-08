import sys
import numbers

def multi(x,y):
    return x * y


if __name__ == "__main__":
    try:
        (n1, n2) = sys.argv[1:3]
        n1 = float(n1)
        n2 = float(n2)
        if isinstance(n1, numbers.Number) and isinstance(n2, numbers.Number):
            print(multi(n1, n2))
    except:
        print("Error")
