from matcher import (
    normalize_all_resumes,
    build_vocabulary,
    compute_idf,
    compute_tfidf_vectors,
    build_jd_vectors,
    rank_candidates
)

from data import JOB_DESCRIPTIONS


def main():
    # Step 1: Normalize resumes
    normalized_resumes = normalize_all_resumes()
    # Step 2: Build vocabulary
    vocabulary = build_vocabulary(
        normalized_resumes
    )
    # Step 3: Compute IDF
    idf_scores = compute_idf(
        normalized_resumes,
        vocabulary
    )
    # Step 4: Compute TF-IDF vectors
    tfidf_vectors = compute_tfidf_vectors(
        normalized_resumes,
        vocabulary,
        idf_scores
    )
    # Step 5: Build JD vectors
    jd_vectors = build_jd_vectors(
        vocabulary
    )
    # Step 6: Rank candidates
    rankings = rank_candidates(
        normalized_resumes,
        tfidf_vectors,
        jd_vectors
    )
    # Final Output
    print("\n=== FINAL MATCHING RESULTS ===\n")
    for jd_id, candidates in rankings.items():
        jd_info = JOB_DESCRIPTIONS[jd_id]
        print(
            f"{jd_id} — "
            f"{jd_info['Company']} "
            f"({jd_info['Role']})"
        )
        result = []
        for name, score in candidates:
            result.append(
                f"{name} ({score:.2f})"
            )
        print(", ".join(result))
        print()


if __name__ == "__main__":
    main()