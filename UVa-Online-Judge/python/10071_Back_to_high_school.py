def displacement_twice_time(v: int, t: int) -> int:
    """
    Return twice times the displacement of an object based on the velocity and time
    """
    return 2 * v * t


def main() -> None:
    while True:
        try:
            v, t = map(int, input().split())
        except EOFError:
            break
        print(displacement_twice_time(v=v, t=t))


if __name__ == "__main__":
    main()
