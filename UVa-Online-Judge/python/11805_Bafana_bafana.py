def get_player_who_gives_ball(n: int, k: int, p: int) -> int:
    out = (k + p) % n
    if out == 0:
        return n
    return out 


def main() -> None:
    cases = int(input())
    i = 1
    while i <= cases:
        n, k, p = map(int, input().split())
        print(f"Case {i}: {get_player_who_gives_ball(n=n, k=k, p=p)}")
        i += 1


if __name__ == "__main__":
    main()
