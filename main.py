from quiz import Quiz
from quiz_data import get_default_quizzes

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


def play_quiz(quizzes):
    """퀴즈를 하나씩 출제하고, 점수(0~100)를 돌려준다."""
    if len(quizzes) == 0:
        print("\n📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.\n")
        return None

    total = len(quizzes)
    correct_count = 0
    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)\n")

    for number, quiz in enumerate(quizzes, start=1):
        print("-" * 40)
        quiz.display(number)
        user_answer = ask_number("정답 입력: ", 1, len(quiz.choices))
        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!\n")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.\n")

    score = int(correct_count / total * 100)
    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40 + "\n")
    return score

def ask_text(prompt):
    """빈 값이 아닌 글자를 받을 때까지 다시 묻는다."""
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("⚠️ 빈 값은 입력할 수 없습니다. 다시 입력하세요.")


def add_quiz(quizzes):
    """사용자에게 문제, 선택지 4개, 정답을 입력받아 새 퀴즈를 추가한다."""
    print("\n📌 새로운 퀴즈를 추가합니다.\n")
    question = ask_text("문제를 입력하세요: ")

    choices = []
    for number in range(1, 5):
        choice = ask_text(f"선택지 {number}: ")
        choices.append(choice)

    answer = ask_number("정답 번호 (1-4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)
    print(f"\n✅ 퀴즈가 추가되었습니다! (현재 총 {len(quizzes)}개)\n")


def main():
    quizzes = get_default_quizzes()
    while True:
        show_menu()
        choice = ask_number("선택: ", 1, len(MENU_ITEMS))
        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            add_quiz(quizzes)
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