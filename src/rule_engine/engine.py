from src.rule_engine.rules import RULES


class RuleEngine:

    def apply(self, profile: dict, domain_scores: dict) -> dict:
        """
            Apply expert rules on top of scorer output
            Add statistics
        """
        adjusted = domain_scores.copy()
        # How many rules improved the domain
        rule_hits = {}

        for rule in RULES:
            if rule["if"](profile):
                for domain, boost in rule["effect"].items():
                    adjusted[domain] = adjusted.get(domain, 0) + boost
                    rule_hits[domain] = rule_hits.get(domain, 0) + 1

        final_scores = self._normalize(adjusted)

        return final_scores, rule_hits

    def _normalize(self, scores: dict) -> dict:
        """Convert raw scores to probabilities"""
        total = sum(scores.values())
        if total == 0:
            return {}
        return {
            domain: round(score / total, 2)
            for domain, score in scores.items()
        }
