'''create a ai chatbot to handle customer queries for a retail website,
the chatbot bot should be able to respond to questions about product availability,
order status, Account Issues, product inquiries or general questions.'''

# Sample customer queries
queries = [
    "Is the new smartphone model available in stock?",
    "What is the status of my order #12345?",
    "I am having trouble logging into my account. Can you help?",
    "Can you provide more details about the features of the laptop?",
    "What are your store hours and return policy?"
]
# Function to classify customer queries
def classify_query(query):
    query_lower = query.lower()
    if "available" in query_lower or "in stock" in query_lower:
        return "Product Availability"
    elif "status" in query_lower or "order" in query_lower:
        return "Order Status"
    elif "trouble logging in" in query_lower or "account" in query_lower:
        return "Account Issues"
    elif "details" in query_lower or "features" in query_lower:
        return "Product Inquiries"
    else:
        return "General Questions"
# Classify and print the category of each query
for query in queries:
    category = classify_query(query)
    print(f"Query categorized as: {category}\n")
    

    