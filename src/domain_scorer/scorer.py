from collections import defaultdict
from src.knowledge_base.loader import load_kb


class DomainScorer:
    def __init__(self):
        kb = load_kb()
        # domain's weights
        self.scores = defaultdict(float)

        self.subject_weights = kb["mappings"]["subjects"]
        self.skill_weights = kb["mappings"]["skills"]

    def predict_domains(self, profile: dict) -> dict:
        """Determine the domain"""
        self.scores.clear()

        self._process_subjects(profile.get("subjects", []))
        self._process_skills(profile.get("skills", {}))

        return self._normalize()

    def _process_subjects(self, subjects):
        """Compute subject weights"""
        for subject in subjects:
            if subject in self.subject_weights:
                for domain, weight in self.subject_weights[subject].items():
                    self.scores[domain] += weight

    def _process_skills(self, skills):
        """Compute skill weights"""
        for skill, value in skills.items():
            if skill in self.skill_weights:
                for domain, weight in self.skill_weights[skill].items():
                    self.scores[domain] += weight * value  # importance of skill

    def _process_preferences(self, preferences):
        """Compute preference weights"""
        for preference in preferences:
            if preference in self.preference_weights:
                for domain, weight in self.preference_weights[preference].items():
                    self.scores[domain] += weight

    def _normalize(self):
        """Convert raw scores to probabilities"""
        total = sum(self.scores.values())

        if total == 0:
            return {}

        return {
            domain: round(score / total, 2)
            for domain, score in self.scores.items()
        }