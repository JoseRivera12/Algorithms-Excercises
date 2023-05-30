def different_problem(num1, num2) -> int:
    return abs(num1 - num2)

def main():
    while True:
        try:
            num1, num2 = map(int, input().split())
        except EOFError:
            break
        print(different_problem(num1, num2))
    
if __name__ == "__main__":
    main()