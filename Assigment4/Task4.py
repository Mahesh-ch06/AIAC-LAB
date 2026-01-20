'''create a predicts a person’s Indian Zodiac sign based on their birth year
March → Mesha
April → Vrishabha
May → Mithuna
June → Karka
July → Simha
August → Kanya
September → Tula
October → Vrischika
November → Dhanu
December → Makara
January → Kumbha
February → Meena
example
input: March
output: Mesha
input: May
output: Mithuna
'''
def indian_zodiac_sign(month):
    zodiac_signs = {
        'march': 'Mesha',
        'april': 'Vrishabha',
        'may': 'Mithuna',
        'june': 'Karka',
        'july': 'Simha',
        'august': 'Kanya',
        'september': 'Tula',
        'october': 'Vrischika',
        'november': 'Dhanu',
        'december': 'Makara',
        'january': 'Kumbha',
        'february': 'Meena'
    }
    
    month_lower = month.lower()
    return zodiac_signs.get(month_lower, "Invalid month")
# Example usage
input_month = "March"
result = indian_zodiac_sign(input_month)
print(result)  # Output: Mesha
# Example usage
input_month2 = "May"
result2 = indian_zodiac_sign(input_month2)
print(result2)  # Output: Mithuna