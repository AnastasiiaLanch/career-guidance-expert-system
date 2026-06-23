
RULES = [
    # subject + skill combination
    {
        "name": "Math + Programming -> Technology",
        "if": lambda p: (
            "Mathematics" in p.get("subjects", [])
            and p.get("skills", {}).get("Programming", 0) >= 3
        ),
        "effect": {"Technology": 0.2}
    },

    {
        "name": "Physics + Problem Solving → Engineering",
        "if": lambda p: (
            "Physics" in p.get("subjects", [])
            and p.get("skills", {}).get("Problem Solving", 0) >= 3
        ),
        "effect": {"Engineering": 0.2}
    },

    {
        "name": "Biology + Empathy → Medicine",
        "if": lambda p: (
            "Biology" in p.get("subjects", [])
            and p.get("skills", {}).get("Empathy", 0) >= 3
        ),
        "effect": {"Medicine": 0.25}
    },

    {
        "name": "CS + Analytical Thinking → Technology",
        "if": lambda p: (
            "Computer Science" in p.get("subjects", [])
            and p.get("skills", {}).get("Analytical Thinking", 0) >= 3
        ),
        "effect": {"Technology": 0.25}
    },

    # Preferences

    {
        "name": "Working with data",
        "if": lambda p: "Working with data" in p.get("preferences", []),
        "effect": {"Technology": 0.1, "Business": 0.1}
    },

    {
        "name": "Working with people",
        "if": lambda p: "Working with people" in p.get("preferences", []),
        "effect": {"Social Sciences": 0.1, "Medicine": 0.1}
    },

    {
        "name": "Building systems",
        "if": lambda p: "Building systems" in p.get("preferences", []),
        "effect": {"Technology": 0.15, "Engineering": 0.15}
    },

    {
        "name": "Creative work",
        "if": lambda p: "Creative work" in p.get("preferences", []),
        "effect": {"Creative": 0.2}
    },

    # Constraints

    {
        "name": "High salary",
        "if": lambda p: "High salary" in p.get("constraints", []),
        "effect": {"Technology": 0.15, "Business": 0.15}
    },

    {
        "name": "Fast career growth",
        "if": lambda p: "Fast career growth" in p.get("constraints", []),
        "effect": {"Technology": 0.2}
    }
]