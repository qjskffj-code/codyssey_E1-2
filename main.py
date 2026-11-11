import json
from pathlib import Path

from quiz import Quiz
from quiz_data import get_default_quizzes

STATE_FILE = Path(__file__).parent / "state.json"

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


def show_quiz_list(quizzes):
    """등록된 퀴즈의 문제 목록을 출력한다."""
    if len(quizzes) == 0:
        print("\n📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.\n")
        return

    print(f"\n📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)\n")
    print("-" * 40)
    for number, quiz in enumerate(quizzes, start=1):
        print(f"[{number}] {quiz.question}")
    print("-" * 40 + "\n")


def update_best_score(score, best_score):
    """이번 점수와 최고 점수를 비교해서, 더 높은 쪽을 돌려준다."""
    if score is None:
        return best_score
    if best_score is None or score > best_score:
        print("🎉 새로운 최고 점수입니다!\n")
        return score
    print(f"현재 최고 점수는 {best_score}점입니다.\n")
    return best_score


def show_best_score(best_score):
    """최고 점수를 출력한다."""
    if best_score is None:
        print("\n📭 아직 퀴즈를 풀지 않았습니다. 1번으로 먼저 도전해 보세요!\n")
    else:
        print(f"\n🏆 최고 점수: {best_score}점\n")


def load_state():
    """state.json에서 퀴즈 목록과 최고 점수를 불러온다. 문제가 있으면 기본값을 쓴다."""
    if not STATE_FILE.exists():
        print("📂 저장 파일이 없어 기본 퀴즈로 시작합니다.")
        return get_default_quizzes(), None

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        quizzes = []
        for item in data["quizzes"]:
            if len(item["choices"]) != 4 or item["answer"] not in (1, 2, 3, 4):
                raise ValueError("퀴즈 형식이 올바르지 않습니다.")
            quizzes.append(Quiz(item["question"], item["choices"], item["answer"]))
        best_score = data.get("best_score")

        score_text = "없음" if best_score is None else f"{best_score}점"
        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {score_text})")
        return quizzes, best_score
    except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError):
        print("⚠️ 저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
        return get_default_quizzes(), None


def save_state(quizzes, best_score):
    """퀴즈 목록과 최고 점수를 state.json에 저장한다."""
    quiz_list = []
    for quiz in quizzes:
        quiz_list.append(quiz.to_dict())
    data = {"quizzes": quiz_list, "best_score": best_score}

    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        print("⚠️ 파일을 저장하는 중 오류가 발생했습니다.")


def main():
    quizzes, best_score = load_state()
    try:
        while True:
            show_menu()
            choice = ask_number("선택: ", 1, len(MENU_ITEMS))
            if choice == 1:
                score = play_quiz(quizzes)
                best_score = update_best_score(score, best_score)
                save_state(quizzes, best_score)
            elif choice == 2:
                add_quiz(quizzes)
                save_state(quizzes, best_score)
            elif choice == 3:
                show_quiz_list(quizzes)
            elif choice == 4:
                show_best_score(best_score)
            else:
                save_state(quizzes, best_score)
                print("👋 프로그램을 종료합니다.")
                break
    except (KeyboardInterrupt, EOFError):
        save_state(quizzes, best_score)
        print("\n\n👋 입력이 중단되어 저장 후 안전하게 종료합니다.")


if __name__ == "__main__":
    main()

    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 입력이 중단되어 프로그램을 안전하게 종료합니다.")