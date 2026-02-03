# llm/matcher.py

import json
import subprocess


def match_candidate_to_job(
    jd_text: str,
    candidate_roles: list,
    candidate_skills: list,
    candidate_experience: int,
):
    prompt = f"""
You are an expert technical recruiter and hiring analyst.

### Candidate Profile
- Target Roles: {candidate_roles}
- Total Experience: {candidate_experience} years
- Skills: {candidate_skills}

### Job Description
\"\"\"
{jd_text}
\"\"\"

### Task
Evaluate how well the candidate matches the job.

Return ONLY valid JSON using this exact schema:
{{
  "is_match": true | false,
  "match_score": number (0-100),
  "matched_roles": [string],
  "matched_skills": [string],
  "missing_skills": [string],
  "experience_fit": string,
  "reasoning": string
}}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="ignore",
        capture_output=True,
    )

    output = result.stdout.strip()
    start = output.find("{")
    end = output.rfind("}") + 1

    if start == -1 or end == -1:
        raise ValueError("LLM did not return valid JSON")

    return json.loads(output[start:end])
