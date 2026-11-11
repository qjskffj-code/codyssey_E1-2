MENU_ITEMS = ["퀴즈 풀기", "퀴즈 추가", "퀴즈 목록", "점수 확인", "종료"]


def show_menu():
    """메뉴 화면을 출력한다."""
    print("=" * 40)
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    for number, name in enumerate(MENU_ITEMS, start=1):
        print(f"{number}. {name}")
    print("=" * 40)


def ask_number(prompt, min_value, max_value):
    """min~max 사이의 숫자를 받을 때까지 계속 다시 묻는다."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("⚠️ 아무것도 입력하지 않았습니다. 숫자를 입력하세요.")
            continue
        try:
            number = int(raw)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        if number < min_value or number > max_value:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        return number


def main():
    while True:
        show_menu()
        choice = ask_number("선택: ", 1, len(MENU_ITEMS))
        if choice == 1:
            print("\n(준비 중) 퀴즈 풀기\n")
        elif choice == 2:
            print("\n(준비 중) 퀴즈 추가\n")
        elif choice == 3:
            print("\n(준비 중) 퀴즈 목록\n")
        elif choice == 4:
            print("\n(준비 중) 점수 확인\n")
        else:
            print("👋 프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 입력이 중단되어 프로그램을 안전하게 종료합니다.")