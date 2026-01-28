'''classify the post posted on social media into acceptable or offensive or spam.'''
posts = [
    "Check out this amazing deal on electronics!",
    "You are so stupid and ugly!",
    "Win a free iPhone now!!! Click here!",
    "Had a great day at the park with friends.",
    "This is the worst product I have ever bought.",
    "Congratulations! You've been selected for a prize."
]
# Function to classify posts
def classify_post(post):
    post_lower = post.lower()
    offensive_keywords = ["stupid", "ugly", "idiot", "hate", "dumb"]
    spam_keywords = ["win", "free", "click here", "selected", "prize", "deal"]
    
    if any(word in post_lower for word in offensive_keywords):
        return "Offensive"
    elif any(word in post_lower for word in spam_keywords):
        return "Spam"
    else:
        return "Acceptable"
# Classify and print the category of each post
for post in posts:
    category = classify_post(post)
    print(f"Post categorized as: {category}\n")

'''classify the post posted on social media into acceptable or offensive or spam.
Post: “You are an idiot and I hate you.”
Category: Offensive
'''
post = "You are an idiot and I hate you."
category = classify_post(post)

print(f"Post: \"{post}\"\nCategory: {category}")

'''classify the post posted on social media into acceptable or offensive or spam.
Post: “Congratulations! You've won a free vacation.”
Category: Spam
Post: “Had a wonderful time with family.”
Category: Acceptable
Post: “This is a dumb idea.”
Category: Offensive
'''
post_list = [
    "Congratulations! You've won a free vacation.",
    "Had a wonderful time with family.",
    "This is a dumb idea."
]
for post in post_list:
    category = classify_post(post)
    print(f"Post: \"{post}\"\nCategory: {category}\n")

