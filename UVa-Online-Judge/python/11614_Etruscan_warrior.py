import math

def get_etruscan_warrior_formation(warriors: int) -> int:
    return int((math.sqrt(1+warriors*8) - 1) / 2)


def main() -> None:
    cases = int(input())
    while cases:
        warriors = int(input())
        print(get_etruscan_warrior_formation(warriors=warriors))
        cases -= 1


if __name__ == "__main__":
    main()
