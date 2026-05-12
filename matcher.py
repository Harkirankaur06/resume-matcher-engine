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
    """
    vocabulary_set = set()
    for resume_data in normalized_resumes.values():
        skills = resume_data["Skills"]
        for skill in skills:
            vocabulary_set.add(skill)
    vocabulary = sorted(list(vocabulary_set))
    return vocabulary

def compute_idf(normalized_resumes, vocabulary):
    """
    Compute IDF for every skill in vocabulary.
    """
    total_resumes = len(normalized_resumes)
    idf_scores = {}
    for skill in vocabulary:
        document_frequency = 0
        # Count resumes containing the skill
        for resume_data in normalized_resumes.values():
            if skill in resume_data["Skills"]:
                document_frequency += 1
        # IDF formula
        idf = math.log(total_resumes / document_frequency)
        idf_scores[skill] = idf
    return idf_scores

def compute_tfidf_vectors(normalized_resumes, vocabulary, idf_scores):
    """
    Compute TF-IDF vector for each resume.
    """
    tfidf_vectors = {}
    for resume_id, resume_data in normalized_resumes.items():
        skills = resume_data["Skills"]
        total_skills = len(skills)
        vector = []
        for skill in vocabulary:
            # Skill exists in resume
            if skill in skills:
                tf = 1 / total_skills
                tfidf = tf * idf_scores[skill]
                vector.append(tfidf)
            else:
                vector.append(0.0)
        tfidf_vectors[resume_id] = vector
    return tfidf_vectors

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
    # Compute IDF scores
    idf_scores = compute_idf(
        normalized_resumes,
        vocabulary
    )
    print("\n--- IDF SCORES ---\n")

    for skill, score in idf_scores.items():
        print(f"{skill}: {round(score, 4)}")
    # Compute TF-IDF vectors
    tfidf_vectors = compute_tfidf_vectors(
        normalized_resumes,
        vocabulary,
        idf_scores
    )
    print("\n--- TF-IDF VECTORS ---\n")
    for resume_id, vector in tfidf_vectors.items():
        print(f"{resume_id}:")
        print(vector)
        print()