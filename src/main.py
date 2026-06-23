from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.domain_scorer.scorer import DomainScorer
from src.rule_engine.engine import RuleEngine
from src.confidence_scorer.scorer import ConfidenceScorer
from src.recommendation.engine import RecommendationEngine

from src.questionnaire.engine import QuestionnaireEngine

app = FastAPI()

engine = QuestionnaireEngine()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class RecommendationRequest(BaseModel):
    subjects: list[str]
    skills: dict[str, int]
    preferences: list[str]
    constraints: list[str]


@app.get("/")
def home():
    return {"message": "Career Guidance API"}


@app.post("/recommend")
def recommend(student_profile: RecommendationRequest):
    profile_dict = student_profile.model_dump()
    domain_scores = DomainScorer().predict_domains(profile_dict)

    rule_scores, rule_hits = RuleEngine().apply(
        profile_dict,
        domain_scores
    )
    # confidence scores
    conf_scores = ConfidenceScorer().compute(
        profile_dict,
        rule_scores,
        rule_hits
    )
    # recommendations (output)
    recs = RecommendationEngine().generate(conf_scores)

    return recs


class AnswerRequest(BaseModel):
    answer: list | dict


@app.get("/question")
def get_question():
    """Get the question"""
    block = engine.get_current_question()

    if block is None:
        return {
            "finished": True
        }

    return {
        "question": block["question"],
        "type": block["type"],
        "answer_format": block["type"],
        "options": block.get("options", []),
        "scale": block.get("scale", [1, 2, 3, 4, 5]),
        "finished": engine.is_finished()
    }


@app.post("/answer")
def submit_answer(response: AnswerRequest):
    engine.submit_answer(response.answer)

    if engine.is_finished():
        # print(engine.session["answers"])
        student_profile = engine.finish()

        # domain scoring
        domain_scores = DomainScorer().predict_domains(student_profile)
        # rule engine
        rule_scores, rule_hits = RuleEngine().apply(
            student_profile,
            domain_scores
        )
        # confidence
        conf_scores = ConfidenceScorer().compute(
            student_profile,
            rule_scores,
            rule_hits
        )
        # recommendations
        recs = RecommendationEngine().generate(conf_scores)

        return {
            "finished": True,
            "profile": student_profile,
            "recommendations": recs
        }

    return {
        "finished": False,
        "question": engine.get_current_question()
    }

