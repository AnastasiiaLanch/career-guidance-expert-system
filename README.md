# Career Guidance Expert System

## Overview

Career Guidance Expert System is a rule-based career recommendation system designed for high school students

The system collects information about:

* preferred school subjects
* skills and competencies
* work preferences
* career constraints and priorities

Based on the collected profile, the system identifies the most relevant professional domains and generates recommendations for:

* university degree programs
* academic subjects
* potential career paths

---

# System Architecture

The system is fully **knowledge-base driven** - questionnaire structure is generated dynamically

```text
Knowledge Base
      ↓
Questionnaire
      ↓
Student Profile Builder
      ↓
Domain Scorer
      ↓
Rule Engine
      ↓
Confidence Scorer
      ↓
Recommendation Engine
      ↓
Career Recommendations
```

Detailed workflow:

```text
Student
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
Questionnaire
   ↓
Knowledge Base
   ↓
Student Profile
   ↓
Domain Scorer
   - evaluates subjects
   - evaluates skills
   ↓
Rule Engine
   - applies expert rules
   - adjusts domain scores
   ↓
Confidence Scorer
   - estimates confidence level
   - ranks domains
   ↓
Recommendation Engine
   - selects top domains
   - recommends:
       • degree programs
       • academic subjects
       • career paths
```

---

# Project Structure

```text
src/

├── main.py
│
├── questionnaire/
│   ├── questions.py
│   └── engine.py
│
├── student_profile/
│   └── builder.py
│
├── domain_scorer/
│   └── scorer.py
│
├── rule_engine/
│   ├── rules.py
│   └── engine.py
│
├── confidence_scorer/
│   └── scorer.py
│
├── recommendation/
│   └── engine.py
│
├── knowledge_base/
│   ├── loader.py
│   ├── subjects.json
│   ├── skills.json
│   ├── preferences.json
│   ├── constraints.json
│   ├── domains.json
│   ├── mappings.json
│   ├── degree_programs.json
│   ├── recommended_subjects.json
│   └── careers.json
│
└── frontend/
    ├── src/
    │   ├── api.js
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── styles.css
    │
    ├── index.html
    ├── package.json
    └── vite.config.js
```

---

# Knowledge Base

## Data Sources

### Subjects

List of school subjects:

```text
subjects.json
```

Examples:

* Mathematics
* Physics
* Economics
* Literature

---

### Skills

List of student skills:

```text
skills.json
```

Examples:

* Analytical Thinking
* Programming
* Communication
* Leadership

---

### Preferences

List of student preferences:

```text
preferences.json
```

Examples:

* Working with data
* Working with people
* Building systems
* Creative work

---

### Constraints

List of student constraints:

```text
constraints.json
```

Examples:

* High salary
* Job stability
* Fast career growth
* Helping people

---

### Domains

Professional domains:

```text
domains.json
```

Examples:

* Technology
* Business
* Healthcare
* Humanities

---

### Domain Mappings

Mappings between:

* subjects
* skills
* domains

Stored in:

```text
mappings.json
```

These mappings are used by the Domain Scorer

---

## Recommendation Data

Knowledge base contains domain-specific recommendations

### Degree Programs

```text
degree_programs.json
```

Examples:

* Computer Science
* Economics
* Artificial Intelligence

### Recommended Subjects

```text
recommended_subjects.json
```

Examples:

* Algorithms
* Statistics
* Finance

### Careers

```text
careers.json
```

Examples:

* Software Engineer
* Data Scientist
* Economist

---

# Questionnaire Module

## Questions

The questionnaire consists of four blocks:

1. Preferred subjects
2. Skills self-assessment
3. Work preferences
4. Career priorities and constraints

Generated from the knowledge base:

```text
knowledge_base → questionnaire engine → frontend
```

Defined in:

```text
questionnaire/questions.py
```

---

## Questionnaire Engine

Responsible for:

* question extraction
* storing users answers
* managing questionnaire state
* generating a completed questionnaire result
* controlling progression

Flow:

```text
build_questions() → engine → frontend
```

Implemented in:

```text
questionnaire/engine.py
```

---

# Student Profile Builder

Converts raw questionnaire answers into a structured student profile.

Implemented in:

```text
student_profile/builder.py
```

Output:

```json
{
  "subjects": [...],
  "skills": {...},
  "preferences": [...],
  "constraints": [...]
}
```

---

# Domain Scorer

Evaluates match between student profile and domains

Implemented in:

```text
domain_scorer/scorer.py
```

Uses:

* subject → domain mapping
* skill → domain mapping
* weighted scoring system

Output:

```json
{
  "Technology": 0.68,
  "Business": 0.32
}
```

---

# Rule Engine

Applies expert rules on top of scoring system

Implemented in:

```text
rule_engine/
```

Components:

### rules.py

Contains expert rules; takes into account preferences and constraints as well as preferred subjects and skills

Examples:

* strong programming skills → Technology boost
* leadership + economics → Business boost

### engine.py

Applies rules and modifies domain scores

---

# Confidence Scorer

Calculates confidence levels for each domain recommendation

Implemented in:

```text
confidence_scorer/scorer.py
```

Combines:

* domain scores
* activated expert rules

Output example:

```json
{
  "Technology": {
    "score": 9
  },
  "Business": {
    "score": 6
  }
}
```

---

# Recommendation Engine

Generates final recommendations

Implemented in:

```text
recommendation/engine.py
```

Responsibilities:

* rank domains
* select top recommendations
* generate:
  * degree programs 
  * recommended subjects 
  * career paths


---

# Backend

FastAPI application.

Default URL:

```text
http://127.0.0.1:8000
```

Endpoints:

```text
GET /question
```
Returns dynamic question from knowledge base

```text
POST /answer
```
Accepts answers and returns:
* next question OR
* final profile + recommendations

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## main.py

```text
src/main.py
```

Application entry point.

Responsible for:

* FastAPI application configuration;
* CORS configuration;
* API endpoint definition;
* questionnaire management;
* integration of all expert system modules:

  * Questionnaire Engine;
  * Student Profile Builder;
  * Domain Scorer;
  * Rule Engine;
  * Confidence Scorer;
  * Recommendation Engine.

The file orchestrates the complete recommendation pipeline:

---

# Frontend

React + Vite application.

Default URL:

```text
http://localhost:5173
```

Features:

* dynamic questionnaire
* multi-select answers
* rating-based skill input
* recommendation dashboard

---

# Running the Project

From the project root:

```bash
bash run.sh
```

Script starts:

* FastAPI backend
* React frontend

---

# Future Improvements

Potential future extensions:

* full UI redesign (card-based flow)
* progress tracking (step indicator)
* explanation engine ("why this recommendation")
* user history storage
* ML-based scoring layer

---

# Author 

Created by [Anastasiia Lanchinskaia](https://github.com/AnastasiiaLanch)

Career Guidance Expert System  
FastAPI • React • Python • Rule-based system