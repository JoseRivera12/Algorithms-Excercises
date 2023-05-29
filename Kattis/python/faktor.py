# Desigualdades
"""
C/A = I

math.ceil(C/A)

I-1 < C/A <= I

(I - 1) * A < C <= I
(I-1)*A - 1 = Next element to get ceil of value to get exactly the first element

"""


def get_faktor(i: int, a: int):
    return ((i-1)*a + 1)

def main():
    a, i = map(int, input().split())
    print(get_faktor(i=i, a=a))

if __name__ == "__main__":
    main()
