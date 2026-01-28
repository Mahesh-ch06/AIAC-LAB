'''create a feedback analysis system for university feedback recieved from students,
it should be categorized into positive, negative, neutral feedback.'''
# Sample feedback data
feedbacks = [
    "The course was very informative and the professor was excellent!",
    "I found the lectures to be boring and unengaging.",
    "The assignments were okay, nothing special.",
    "Great learning experience, I enjoyed every part of it.",
    "The material was outdated and not relevant to current industry standards.",
    "It was an average course, I learned some new things but nothing extraordinary."
]
# Function to classify feedback
def classify_feedback(feedback):
    feedback_lower = feedback.lower()
    positive_keywords = ["excellent", "great", "enjoyed", "informative", "good", "fantastic", "amazing"]
    negative_keywords = ["boring", "unengaging", "outdated", "dissatisfied", "poor", "bad", "terrible"]
    
    if any(word in feedback_lower for word in positive_keywords):
        return "Positive"
    elif any(word in feedback_lower for word in negative_keywords):
        return "Negative"
    else:
        return "Neutral"
# Classify and print the category of each feedback
for feedback in feedbacks:
    category = classify_feedback(feedback)
    print(f"Feedback categorized as: {category}\n")


'''create a feedback analysis system for university feedback recieved from students,
it should be categorized into positive, negative, neutral feedback.
Feedback: “The course content was boring and confusing.”
Sentiment: Negative
'''
feedback = "The course content was boring and confusing."
sentiment = classify_feedback(feedback)
print(f"Feedback: \"{feedback}\"\nSentiment: {sentiment}")

'''create a feedback analysis system for university feedback recieved from students,
it should be categorized into positive, negative, neutral feedback.

Feedback: “I really enjoyed the practical sessions and found them very helpful.”
Sentiment: Positive

Feedback: “The assignments helped me learn a lot.”
Sentiment: Positive

Feedback: “The syllabus was okay, nothing special.”
Sentiment: Neutral

Feedback: “The exams were unfair and too difficult.”
Sentiment: Negative
'''
feedback_list = [
    "I really enjoyed the practical sessions and found them very helpful.",
    "The assignments helped me learn a lot.",
    "The syllabus was okay, nothing special.",
    "The exams were unfair and too difficult."
]
for feedback in feedback_list:
    sentiment = classify_feedback(feedback)
    print(f"Feedback: \"{feedback}\"\nSentiment: {sentiment}\n")


