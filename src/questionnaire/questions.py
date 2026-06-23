# structured question schema for questionnaire engine
from src.knowledge_base.loader import load_kb

kb = load_kb()


def build_questions():
    """
    Generates questionnaire dynamically from knowledge base
    """
    return [
        {
            "id": "subjects",
            "type": "multi_select",
            "question": "Which subject do you like?",
            "options": kb["subjects"]
        },
        {
            "id": "skills",
            "type": "rating",
            "question": "Rate yout skills (1-5)?",
            "options": kb["skills"]
        },
        {
            "id": "preferences",
            "type": "multi_select",
            "question": "What do you prefer working with?",
            "options": kb["preferences"]
        },
        {
            "id": "constraints",
            "type": "multi_select",
            "question": "What matters most to you?",
            "options": kb["constraints"]
        }
    ]

