# Classify the following given text as spam or not spam and display the result as spam or not spam

def classify_text(text):
    spam_keywords = ['win', 'free', 'prize', 'click', 'buy now', 'limited time offer', 'congratulations']
    text_lower = text.lower()
    
    for keyword in spam_keywords:
        if keyword in text_lower:
            return "spam"
    
    return "not spam"
# Example usage
input_text = "Congratulations! You have won a free prize. Click here to claim it."
result = classify_text(input_text)
print(result)  # Output: spam
# Example usage
input_text2 = "Hello, I hope you are having a great day!"
result2 = classify_text(input_text2)
print(result2)  # Output: not spam
# Example usage
input_text3 = "Limited time offer! Buy now and save big."
result3 = classify_text(input_text3)
print(result3)  # Output: spam
# Example usage
input_text4 = "Congratulations! You have won a free lottery ticket."
result4 = classify_text(input_text4)
print(result4)  # Output: spam
