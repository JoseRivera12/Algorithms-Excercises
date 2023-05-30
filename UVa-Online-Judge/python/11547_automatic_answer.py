def automatic_answer(n: int):
    operation = (((n * 567) / 9 + 7492) * 235) / 47 - 498
    if operation < 0:
        operation *= -1
    return int((operation // 10) % 10)


def main():
    n_cases = int(input())
    for _ in range(n_cases):
        n = int(input())
        print(automatic_answer(n=n))


if __name__ == "__main__":
    main()