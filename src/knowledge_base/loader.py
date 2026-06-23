import json
from pathlib import Path


def load_json(filename: str):
    """
    Safe json loader for knowledge base files
    """
    base_dir = Path(__file__).parent

    file_path = base_dir / filename

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_kb():
    """
    Loads full knowledge base into a single structured dict
    """

    return {
        "subjects": load_json("subjects.json"),
        "skills": load_json("skills.json"),
        "domains": load_json("domains.json"),
        "mappings": load_json("mappings.json"),
        "degree_programs": load_json("degree_programs.json"),
        "recommended_subjects": load_json("recommended_subjects.json"),
        "careers": load_json("careers.json"),
        "preferences": load_json("preferences.json"),
        "constraints": load_json("constraints.json")
    }