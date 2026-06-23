import json
from pathlib import Path


class RecommendationEngine:
    def __init__(self):
        data_dir = Path(__file__).parent.parent / "knowledge_base"
        with open(data_dir / "recommended_subjects.json") as f:
            self.recommended_subjects = json.load(f)

        with open(data_dir / "degree_programs.json") as f:
            self.degree_programs = json.load(f)

        with open(data_dir / "careers.json") as f:
            self.careers = json.load(f)

    def generate(self, confidence_result: dict) -> dict:
        ranked_domains = self._rank_domains(confidence_result)
        subjects = []
        degree_programs = []
        careers = []

        for domain in ranked_domains:
            subjects.extend(
                self.recommended_subjects.get(domain, [])
            )
            degree_programs.extend(
                self.degree_programs.get(domain, [])
            )
            careers.extend(
                self.careers.get(domain, [])
            )

        return {
            "domains": ranked_domains,
            "recommended_subjects": self._unique(subjects),
            "degree_programs": self._unique(degree_programs),
            "careers": self._unique(careers)
            # "confidence": confidence_result
        }

    @staticmethod
    def _rank_domains(confidence_result: dict) -> list:

        ranked = sorted(
            confidence_result.items(),
            key=lambda item: item[1]["score"],
            reverse=True
        )

        return [domain for domain, _ in ranked[:2]]

    @staticmethod
    def _unique(items: list) -> list:

        seen = set()
        result = []

        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)

        return result
