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
    if not vocabulary:
        print("Warning: Vocabulary is empty.")
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
        total_skills = max(len(skills), 1)
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

def build_jd_vectors(vocabulary):
    """
    Build binary vectors for all job descriptions.
    """
    jd_vectors = {}
    for jd_id, jd_data in JOB_DESCRIPTIONS.items():
        # Combine required + preferred skills
        all_skills = (
            jd_data["Required Skills"]
            + ", " +
            jd_data["Preferred Skills"]
        )
        # Normalize skills
        normalized_skills = normalize_skills(
            all_skills,
            SKILL_ALIASES
        )
        # Build binary vector
        vector = []
        for skill in vocabulary:
            if skill in normalized_skills:
                vector.append(1)
            else:
                vector.append(0)
        jd_vectors[jd_id] = vector
    return jd_vectors

def cosine_similarity(vector_a, vector_b):
    """
    Compute cosine similarity between two vectors.
    """
    dot_product = 0
    for a, b in zip(vector_a, vector_b):
        dot_product += a * b
    magnitude_a = math.sqrt(
        sum(value ** 2 for value in vector_a)
    )
    magnitude_b = math.sqrt(
        sum(value ** 2 for value in vector_b)
    )
    # Prevent division by zero
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    similarity = dot_product / (
        magnitude_a * magnitude_b
    )
    return similarity

def rank_candidates(normalized_resumes, tfidf_vectors, jd_vectors):
    """
    Rank candidates for each JD.
    """
    all_rankings = {}
    for jd_id, jd_vector in jd_vectors.items():
        rankings = []
        for resume_id, resume_vector in tfidf_vectors.items():
            score = cosine_similarity(
                resume_vector,
                jd_vector
            )
            candidate_name = normalized_resumes[
                resume_id
            ]["Candidate"]
            rankings.append(
                (candidate_name, round(score, 2))
            )
        # Sort:
        # 1. Higher score first
        # 2. Alphabetical name for ties
        rankings.sort(
            key=lambda x: (-x[1], x[0])
        )
        # Keep top 3
        all_rankings[jd_id] = rankings[:3]
    return all_rankings

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
    # Build JD vectors
    jd_vectors = build_jd_vectors(vocabulary)
    print("\n--- JD VECTORS ---\n")
    for jd_id, vector in jd_vectors.items():
        print(f"{jd_id}:")
        print(vector)
        print()
    # Rank candidates
    rankings = rank_candidates(
        normalized_resumes,
        tfidf_vectors,
        jd_vectors
    )
    print("\n--- FINAL RANKINGS ---\n")
    for jd_id, top_candidates in rankings.items():
        jd_info = JOB_DESCRIPTIONS[jd_id]
        print(
            f"{jd_id} — "
            f"{jd_info['Company']} "
            f"({jd_info['Role']})"
        )
        result = []
        for name, score in top_candidates:
            result.append(f"{name} ({score:.2f})")
        print(", ".join(result))
        print()