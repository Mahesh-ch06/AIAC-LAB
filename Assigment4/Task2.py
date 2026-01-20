'''from the given list of Emotions: [‘happy', 'sad', 'angry', 'excited', 'nervous', ’neutral’]
example : I am so thrilled about the upcoming trip!
output : excited
now classify the emotions based on sentences and display the result as one of the emotions from the list.'''

def classify_emotion(text):
    emotion_keywords = {
        'happy': ['joy', 'pleased', 'delighted', 'glad', 'cheerful'],
        'sad': ['unhappy', 'sorrowful', 'dejected', 'downcast', 'mournful'],
        'angry': ['mad', 'furious', 'irate', 'livid', 'outraged'],
        'excited': ['thrilled', 'elated', 'eager', 'enthusiastic', 'overjoyed'],
        'nervous': ['anxious', 'tense', 'apprehensive', 'uneasy', 'worried'],
        'neutral': ['calm', 'composed', 'unemotional', 'indifferent', 'detached']
    }
    
    text_lower = text.lower()
    
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                return emotion
    
    return "neutral"
# Example usage
input_text = "I am so thrilled about the upcoming trip!"
result = classify_emotion(input_text)
print(result)  # Output: excited
# Example usage
input_text2 = "I feel very anxious before my presentation."
result2 = classify_emotion(input_text2)
print(result2)  # Output: nervous