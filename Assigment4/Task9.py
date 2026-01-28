'''
create data of 5 emails belonging to Biling, Technical Support, Feedback Othes,
write a python program to Classify the emails  into one of the categories
'''
# Sample email data
emails = [
    "Subject: Invoice for your recent purchase\nDear Customer, please find attached the invoice for your recent purchase. If you have any questions, feel free to contact our billing department.",
    "Subject: Technical Support Needed\nHello, I am experiencing issues with my account login. Can you please assist me in resolving this problem?",
    "Subject: Feedback on your service\nI wanted to provide some feedback regarding the excellent service I received from your team last week. Keep up the great work!",
    "Subject: Inquiry about product features\nCould you provide more information about the features of your new product? I am considering making a purchase.",
    "Subject: Complaint about delayed delivery\nI am writing to express my dissatisfaction with the delayed delivery of my order. Please address this issue promptly."
]
# Function to classify emails
def classify_email(email):
    email_lower = email.lower()
    if "invoice" in email_lower or "billing" in email_lower:
        return "Billing"
    elif "technical support" in email_lower or "issues" in email_lower or "assist" in email_lower:
        return "Technical Support"
    elif "feedback" in email_lower or "service" in email_lower:
        return "Feedback"
    else:
        return "Others"
# Classify and print the category of each email
for email in emails:
    category = classify_email(email)
    print(f"Email categorized as: {category}\n")

