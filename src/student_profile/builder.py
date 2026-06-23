# Student Profile
def build_profile(answers: dict) -> dict:
    """
    Converts raw questionnaire answers into a structured student profile.
    """
    subjects = answers.get("subjects", [])
    skills = answers.get("skills", {})
    preferences = answers.get("preferences", [])
    constraints = answers.get("constraints", [])
    # derived_tags = _extract_tags(subjects, skills, preferences)

    return {
        "subjects": subjects,
        "skills": skills,
        "preferences": preferences,
        "constraints": constraints
    }