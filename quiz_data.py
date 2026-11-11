from quiz import Quiz


def get_default_quizzes():
    """처음 실행하거나 저장 파일이 망가졌을 때 쓸 기본 퀴즈 목록을 돌려준다."""
    return [
        Quiz("Python에서 참(True)/거짓(False)을 나타내는 자료형은?",
             ["int", "str", "bool", "list"], 3),
        Quiz("조건이 참인 동안 계속 반복할 때 쓰는 반복문은?",
             ["while", "for", "if", "def"], 1),
        Quiz("클래스로 객체를 만들 때 자동으로 실행되는 메서드는?",
             ["__main__", "__str__", "self", "__init__"], 4),
        Quiz("메서드의 첫 번째 매개변수 self가 가리키는 것은?",
             ["그 메서드를 호출한 객체 자기 자신", "클래스 이름 문자열",
              "프로그램 전체", "가장 마지막에 만든 객체"], 1),
        Quiz("'키(key)와 값(value)'의 쌍으로 데이터를 저장하는 자료형은?",
             ["list", "str", "dict", "int"], 3),
        Quiz("int(\"abc\")처럼 숫자로 바꿀 수 없는 글자를 변환하면 나는 오류는?",
             ["TypeError", "ValueError", "KeyError", "IndexError"], 2),
        Quiz("파이썬 데이터를 JSON 파일에 '쓸' 때 사용하는 함수는?",
             ["json.load", "json.read", "json.open", "json.dump"], 4),
        Quiz("GitHub의 원격 저장소를 내 컴퓨터로 통째로 처음 복사해 오는 명령어는?",
             ["git pull", "git clone", "git push", "git init"], 2),
        Quiz("새 브랜치 feature를 만들면서 바로 그 브랜치로 이동하는 명령어는?",
             ["git merge feature", "git commit -b feature",
              "git checkout -b feature", "git push feature"], 3),
        Quiz("프로그램 실행 중 Ctrl+C를 누르면 발생하는 예외는?",
             ["KeyboardInterrupt", "EOFError", "ValueError", "FileNotFoundError"], 1),
    ]