def get_number_of_soldiers(soldiers_hashmat: int, enemy_soldiers: int) -> int:
    return abs(soldiers_hashmat - enemy_soldiers)

def main():
    while True:
        try:
            soldiers_hashmat, enemy_soldiers = map(int, input().split())
        except EOFError:
            break
        print(get_number_of_soldiers(soldiers_hashmat=soldiers_hashmat, enemy_soldiers=enemy_soldiers))

if __name__ == "__main__":
    main()