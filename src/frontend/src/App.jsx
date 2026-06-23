import { useEffect, useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [type, setType] = useState("");
  const [options, setOptions] = useState([]);
  const [scale, setScale] = useState([1, 2, 3, 4, 5]);

  // multi_select = array
  const [multiAnswer, setMultiAnswer] = useState([]);

  // rating = object (skill → score)
  const [ratingAnswer, setRatingAnswer] = useState({});

  const [finished, setFinished] = useState(false);
  const [result, setResult] = useState(null);

  // question load from backend
  const loadQuestion = async () => {
    const res = await fetch("http://127.0.0.1:8000/question");
    const data = await res.json();

    if (data.finished) {
      setFinished(true);
      setResult(data);
      return;
    }

    setQuestion(data.question);
    setType(data.type || data.answer_format);
    setOptions(data.options || []);
    setScale(data.scale || [1, 2, 3, 4, 5]);

    // reset answers within nexy question transfer
    setMultiAnswer([]);
    setRatingAnswer({});
  };

  useEffect(() => {
    loadQuestion();
  }, []);

  // toggle для multi_select
  const toggleOption = (opt) => {
    if (multiAnswer.includes(opt)) {
      setMultiAnswer(multiAnswer.filter((x) => x !== opt));
    } else {
      setMultiAnswer([...multiAnswer, opt]);
    }
  };

  // rating processing (skill → score)
  const setRating = (skill, value) => {
    setRatingAnswer({
      ...ratingAnswer,
      [skill]: Number(value)
    });
  };

  // question delivery to backend
  const submitAnswer = async () => {
    const answer = type === "rating" ? ratingAnswer : multiAnswer;

    const res = await fetch("http://127.0.0.1:8000/answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answer })
    });

    const data = await res.json();

    if (data.finished) {
      setFinished(true);
      setResult(data);
    } else {
      loadQuestion();
    }
  };

  // =========================
  // FINAL RESULT SCREEN
  // =========================
  if (finished && result) {
    return (
      <div className="container">
        <h1>Your Career Recommendations</h1>

        <div className="result-layout">

          <div className="card">
            <h2>Student Profile</h2>

            <h3>Subjects</h3>
            <ul>
              {(result.profile?.subjects || []).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <h3>Skills</h3>
            <ul>
              {Object.entries(result.profile?.skills || {}).map(
                ([skill, value]) => (
                  <li key={skill}>
                    {skill}: {value}
                  </li>
                )
              )}
            </ul>

            <h3>Preferences</h3>
            <ul>
              {(result.profile?.preferences || []).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <h3>Constraints</h3>
            <ul>
              {(result.profile?.constraints || []).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>

          <div className="card">
            <h2>Recommendations</h2>

            <h3>Degree Programs</h3>
            <ul>
              {(result.recommendations?.degree_programs || []).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <h3>Suggested Subjects</h3>
            <ul>
              {(result.recommendations?.recommended_subjects || []).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <h3>Potential Careers</h3>
            <ul>
              {(result.recommendations?.careers || []).map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>

        </div>
      </div>
    );
  }

  // =========================
  // QUESTION SCREEN
  // =========================
  return (
    <div className="container">
      <h2>Questionnaire</h2>

      <h3>{question}</h3>

      <p>Type: {type}</p>

      {/* =========================
          MULTI SELECT QUESTION
      ========================= */}
      {type === "multi_select" && (
        <div>
          <p>Select multiple:</p>

          {options.map((opt) => (
            <button
              key={opt}
              onClick={() => toggleOption(opt)}
              style={{
                display: "block",
                margin: 5,
                padding: 8,
                background: multiAnswer.includes(opt)
                  ? "lightblue"
                  : "white",
                color: multiAnswer.includes(opt)
                  ? "darkblue"
                  : "black"
              }}
            >
              {opt}
            </button>
          ))}
        </div>
      )}

      {/* =========================
          RATING QUESTION
      ========================= */}
      {type === "rating" && (
        <div>
          <p>Rate each skill (1–5):</p>

          {options.map((skill) => (
            <div key={skill} style={{ marginBottom: 10 }}>
              <span>{skill}</span>

              <select
                onChange={(e) =>
                  setRating(skill, e.target.value)
                }
                style={{ marginLeft: 10 }}
              >
                <option value="">-</option>

                {scale.map((v) => (
                  <option key={v} value={v}>
                    {v}
                  </option>
                ))}
              </select>
            </div>
          ))}
        </div>
      )}

      <br />

      <button onClick={submitAnswer}>
        Submit
      </button>
    </div>
  );
}

export default App;