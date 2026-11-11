class Quiz:
    """퀴즈 한 문제를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number):
        """문제와 선택지를 화면에 출력한다."""
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")
        print()

    def is_correct(self, user_answer):
        """사용자 답이 정답이면 True, 아니면 False를 돌려준다."""
        return user_answer == self.answer
    
    def to_dict(self):
        """JSON으로 저장할 수 있게 dict 형태로 바꿔 돌려준다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


if __name__ == "__main__":
    # 이 파일만 직접 실행했을 때 동작을 확인하는 테스트용 코드
    sample = Quiz(
        "Python의 창시자는?",
        ["Guido", "Linus", "Bjarne", "James"],
        1,
    )
    sample.display(1)
    print("1번 정답?", sample.is_correct(1))
    print("2번 정답?", sample.is_correct(2))