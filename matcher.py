# matcher.py

import math
from data import RESUMES, JOB_DESCRIPTIONS, SKILL_ALIASES

def normalize_skills(raw_skills_string, skill_aliases):
    """
    Normalize raw skills string by splitting, lowercasing, aliasing, and deduplicating.
    """
    # 1. Split the raw string by commas
    raw_tokens = raw_skills_string.split(',')

    # 2. Convert all tokens to lowercase and strip whitespace
    clean_tokens = [token.strip().lower() for token in raw_tokens]
    normalized_skills = []

    # 3. Iterate over the tokens to apply aliases and discard unknowns
    for token in clean_tokens:
        # Since we already split by commas, "machine learning" is naturally treated as one phrase
        if token in skill_aliases:
            normalized_skills.append(skill_aliases[token])

    # 4. Deduplicate the final list (set removes duplicates)
    deduplicated_skills = list(dict.fromkeys(normalized_skills))
    return deduplicated_skills

def normalize_all_resumes():
    """
    Normalize skills for all resumes.
    Returns:
    dict:
        {
            "01": {
                "Candidate": "Arjun Sharma",
                "Skills": ["python", "sql", ...]
            }
        }
    """
    normalized_resumes = {}
    for resume_id, resume_data in RESUMES.items():
        raw_skills = resume_data["Raw Skills"]
        normalized_skills = normalize_skills(
            raw_skills,
            SKILL_ALIASES
        )
        normalized_resumes[resume_id] = {
            "Candidate": resume_data["Candidate"],
            "Skills": normalized_skills
        }
    return normalized_resumes


def build_vocabulary(normalized_resumes):
    """
    Build shared vocabulary from all normalized resumes.
    Returns:
    list:
        Sorted unique skills
    """
    vocabulary_set = set()
    for resume_data in normalized_resumes.values():
        skills = resume_data["Skills"]
        for skill in skills:
            vocabulary_set.add(skill)
    vocabulary = sorted(list(vocabulary_set))
    return vocabulary

# --- Test Block ---
if __name__ == "__main__":
    print("Testing Normalization on Candidate 01...\n")
    raw = RESUMES["01"]["Raw Skills"]
    print(f"RAW: {raw}")
    clean = normalize_skills(raw, SKILL_ALIASES)
    print(f"CLEAN: {clean}")
    # Normalize all resumes
    normalized_resumes = normalize_all_resumes()
    print("\n--- NORMALIZED RESUMES ---\n")
    for resume_id, data in normalized_resumes.items():
        print(
            f"{resume_id} | "
            f"{data['Candidate']} | "
            f"{data['Skills']}"
        )
    # Build vocabulary
    vocabulary = build_vocabulary(normalized_resumes)
    print("\n--- VOCABULARY ---\n")
    print(vocabulary)