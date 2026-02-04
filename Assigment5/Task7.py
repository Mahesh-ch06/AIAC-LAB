def statistics_subject(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    average_score = sum(scores_list) / len(scores_list)
    passed_count = sum(1 for score in scores_list if score >= 40)
    failed_count = sum(1 for score in scores_list if score < 40)

    return {
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "average_score": average_score,
        "passed_count": passed_count,
        "failed_count": failed_count
    }
# Example usage
if __name__ == "__main__":
    scores = [55, 67, 45, 23, 89, 90, 34, 76, 88, 92,
              41, 39, 60, 72, 81, 33, 49, 58, 77, 84,
              91, 38, 44, 53, 66, 70, 79, 82, 95, 100,
              29, 31, 36, 42, 47, 50, 54, 61, 65, 68,
              74, 80, 85, 87, 93, 96, 98, 22, 25, 27,
              30, 32, 35, 37, 40, 43, 46, 48, 51, 52]
    stats = statistics_subject(scores)
    print(f"Highest Score: {stats['highest_score']}")
    print(f"Lowest Score: {stats['lowest_score']}")
    print(f"Average Score: {stats['average_score']:.2f}")
    print(f"Number of Students Passed: {stats['passed_count']}")
    print(f"Number of Students Failed: {stats['failed_count']}")
    