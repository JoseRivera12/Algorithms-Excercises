def get_number_of_points_per_square(iterations: int) -> int:
    return pow((pow(2, iterations) + 1), 2)


def main() -> None:
    iterations = int(input())
    print(get_number_of_points_per_square(iterations=iterations))


if __name__ == "__main__":
    main()
