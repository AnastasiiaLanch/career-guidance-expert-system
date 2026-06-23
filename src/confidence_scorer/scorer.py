from collections import defaultdict


class ConfidenceScorer:

    def compute(self, profile, domain_scores, rule_hits) -> dict:
        result = {}

        max_rule_hits = max(rule_hits.values()) if rule_hits else 1

        for domain, score in domain_scores.items():
            rule_strength = self._normalize_rule_hits(rule_hits, domain, max_rule_hits)
            consistency = self._consistency(profile, domain)

            confidence = (
                0.5 * score +
                0.3 * rule_strength +
                0.2 * consistency
            )

            result[domain] = {
                "score": round(score, 2),
                "confidence": round(confidence, 2)
            }

        return result

    def _normalize_rule_hits(self, rule_hits, domain, max_rule_hits) -> float:
        if max_rule_hits == 0:
            return 0.0
        return rule_hits.get(domain, 0) / max_rule_hits

    def _consistency(self, profile: dict, domain: str) -> float:
        subjects = profile.get("subjects", [])
        skills = profile.get("skills", {})
        preferences = profile.get("preferences", [])

        signals = 0
        total = 3  # фиксированное число проверок ниже

        if domain == "Technology":
            if "Mathematics" in subjects:
                signals += 1
            if "Computer Science" in subjects:
                signals += 1
            if skills.get("Programming", 0) >= 3:
                signals += 1
            if "Working with data" in preferences:
                signals += 1

        elif domain == "Engineering":
            if "Physics" in subjects:
                signals += 1
            if skills.get("Problem Solving", 0) >= 3:
                signals += 1
            if "Building systems" in preferences:
                signals += 1

        elif domain == "Medicine":
            if "Biology" in subjects:
                signals += 1
            if skills.get("Empathy", 0) >= 3:
                signals += 1
            if "Working with people" in preferences:
                signals += 1

        elif domain == "Business":
            if "Economics" in subjects:
                signals += 1
            if "Working with data" in preferences:
                signals += 1

        elif domain == "Creative":
            if "Literature" in subjects:
                signals += 1
            if "Creative work" in preferences:
                signals += 1

        elif domain == "Social Sciences":
            if "History" in subjects:
                signals += 1
            if "Working with people" in preferences:
                signals += 1

        return signals / total
