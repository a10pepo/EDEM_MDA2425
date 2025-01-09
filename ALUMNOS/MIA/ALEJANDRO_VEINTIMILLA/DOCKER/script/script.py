import sys

def suma(a, b):
    return a + b

if __name__ == "__main__":

    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])

        sum = suma(n1, n2)
        print(f"{n1} + {n2} = {sum}")
    except ValueError:
        print("Algun numero esta mal.")
        sys.exit(1)