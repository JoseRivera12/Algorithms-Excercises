def main() -> None:
    while True:
        try:
            val = input()
        except EOFError:
            break
        print(val)


if __name__ == "__main__":
    main()
