'''Generate an online shopping feedback system using nested if-elif-else to categorize feedback into positive, negative, and neutral based on 1-5 rating scale. And analyze space and time complexity of the code.'''

def categorize_feedback(rating):
    if rating >= 1 and rating <= 5:
        if rating >= 4:
            return "Positive"
        elif rating == 3:
            return "Neutral"
        else:  # rating 1 or 2
            return "Negative"
    else:
        return "Invalid rating. Please provide a rating between 1 and 5."

# Example usage
if __name__ == "__main__":
    rating = float(input("Enter your rating (1-5): "))
    category = categorize_feedback(rating)
    print(f"Your feedback is categorized as: {category}")

# Analysis:
# Time Complexity: O(1) - The function performs a constant number of comparisons and returns immediately, regardless of input size.
# Space Complexity: O(1) - No additional data structures are used; only a fixed amount of memory for variables.
