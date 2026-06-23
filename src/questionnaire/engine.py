from src.questionnaire.questions import build_questions
from src.student_profile.builder import build_profile


class QuestionnaireEngine:
    def __init__(self):
        self.questions = build_questions()

        self.session = {
            "current_step": 0,
            "answers": {}
        }

    def get_current_question(self):
        if self.session["current_step"] >= len(self.questions):
            return None

        return self.questions[self.session["current_step"]]

    def submit_answer(self, answer):
        current_block = self.get_current_question()

        if not current_block:
            return

        self.session["answers"][current_block["id"]] = answer
        self.session["current_step"] += 1

    def is_finished(self):
        return self.session["current_step"] >= len(self.questions)

    def finish(self):
        return build_profile(self.session["answers"])