def num_of_sonars(b, h) -> int:
    b -= 2
    h -= 2
    sonars_for_base = b // 3
    sonars_for_height = h // 3
    if b % 3 != 0:
        sonars_for_base += 1
    if h % 3 != 0:
        sonars_for_height += 1   
    return sonars_for_base * sonars_for_height



def main() -> None:
    cases = int(input())
    for _ in range(cases):
        b, h = map(int, input().split())
        print(num_of_sonars(b, h))


if __name__ == "__main__":
    main()
