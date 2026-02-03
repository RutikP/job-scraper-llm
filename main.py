# main.py

from scraper.fetcher import fetch_page, fetch_job_description
from scraper.parser import parse_jobs
from scraper.jd_parser import parse_job_description
from llm.matcher import match_candidate_to_job


def main():
    # -----------------------------
    # Candidate Profile (YOU CHANGE THIS)
    # -----------------------------
    candidate_profile = {
        "roles": ["Account Executive", "Sales Manager"],
        "skills": ["Sales", "CRM", "Negotiation", "Client Management"],
        "experience": 4,
    }

    # -----------------------------
    # Step 1: Fetch all jobs
    # -----------------------------
    html = fetch_page()
    jobs = parse_jobs(html)

    print(f"\nTotal jobs found: {len(jobs)}\n")

    results = []

    # -----------------------------
    # Step 2: Match EACH job
    # -----------------------------
    for idx, job in enumerate(jobs[0:1], start=1):
        print(f"Processing job {idx}/{len(jobs)}: {job['title']}")

        jd_html = fetch_job_description(job["url"])
        jd_text = parse_job_description(jd_html)

        match_result = match_candidate_to_job(
            jd_text=jd_text,
            candidate_roles=candidate_profile["roles"],
            candidate_skills=candidate_profile["skills"],
            candidate_experience=candidate_profile["experience"],
        )

        results.append(
            {
                "title": job["title"],
                "url": job["url"],
                "match_score": match_result["match_score"],
                "is_match": match_result["is_match"],
                "matched_skills": match_result["matched_skills"],
                "missing_skills": match_result["missing_skills"],
                "experience_fit": match_result["experience_fit"],
            }
        )

    # -----------------------------
    # Step 3: Rank jobs by score
    # -----------------------------
    results.sort(key=lambda x: x["match_score"], reverse=True)

    # -----------------------------
    # Step 4: Print ranked results
    # -----------------------------
    print("\n===== JOB MATCH RESULTS (RANKED) =====\n")

    for rank, job in enumerate(results, start=1):
        print(f"{rank}. {job['title']}")
        print(f"   Match Score   : {job['match_score']}")
        print(f"   Is Match      : {job['is_match']}")
        print(f"   Experience Fit: {job['experience_fit']}")
        print(f"   Matched Skills: {job['matched_skills']}")
        print(f"   Missing Skills: {job['missing_skills']}")
        print(f"   URL           : {job['url']}\n")


if __name__ == "__main__":
    main()
