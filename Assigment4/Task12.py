'''create a online learning platform to recommend courses based on user preferences.
like Display only beginner, intermediate, advanced levels.'''
# Sample course data
courses = [
    {"title": "Python for Beginners", "level": "Beginner"},
    {"title": "Data Structures and Algorithms", "level": "Intermediate"},
    {"title": "Advanced Machine Learning", "level": "Advanced"},
    {"title": "Web Development Basics", "level": "Beginner"},
    {"title": "Database Management Systems", "level": "Intermediate"},
    {"title": "Deep Learning Techniques", "level": "Advanced"}
]
# Function to recommend courses based on user preference
def recommend_courses(level):
    recommended = [course for course in courses if course["level"].lower() == level.lower()]
    return recommended
# Get user preference
user_level = input("Enter your preferred course level (Beginner/Intermediate/Advanced): ")
recommended_courses = recommend_courses(user_level)
# Display recommended courses
if recommended_courses:
    print(f"Recommended {user_level} courses:")
    for course in recommended_courses:
        print(f"- {course['title']}")
else:
    print(f"No courses found for the level: {user_level}")
'''create a online learning platform to recommend courses based on user preferences.
like Display only beginner, intermediate, advanced levels.
User Preference: Intermediate
Recommended Intermediate courses:
- Data Structures and Algorithms
- Database Management Systems
'''
user_level = "Intermediate"
recommended_courses = recommend_courses(user_level)
print(f"Recommended {user_level} courses:")
for course in recommended_courses:
    print(f"- {course['title']}")
'''create a online learning platform to recommend courses based on user preferences.
like Display only beginner, intermediate, advanced levels.
User Preference: Beginner
Recommended Beginner courses:
- Python for Beginners
- Web Development Basics
'''
user_level = "Beginner"
recommended_courses = recommend_courses(user_level)
print(f"Recommended {user_level} courses:")
for course in recommended_courses:
    print(f"- {course['title']}")
    