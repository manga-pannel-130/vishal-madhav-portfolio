# guardrails.py


BLOCKED_WORDS = [
    "password",
    "credit card",
    "card number",
    "bank account",
    "account number",
    "phone number",
    "home address",
    "email address",
    "hack",
    "hacking",
    "malware",
    "virus",
    "exploit",
    "weapon",
    "bomb"
]


ABUSIVE_WORDS = [
    "idiot",
    "stupid",
    "dumb",
    "useless",
    "shut up"
]


OFF_TOPIC_KEYWORDS = [
    "weather",
    "politics",
    "cricket score",
    "football score",
    "movie recommendation",
    "stock price",
    "bitcoin price",
    "recipe",
    "joke"
]


def check_guardrails(user_input):

    text = user_input.lower().strip()

    # Sensitive or harmful requests
    for word in BLOCKED_WORDS:
        if word in text:
            return (
                "I can only provide information related to Vishal's "
                "projects, skills, education, and career goals. "
                "I cannot provide private, sensitive, or harmful information."
            )

    # Abusive language
    for word in ABUSIVE_WORDS:
        if word in text:
            return (
                "Let's keep the conversation respectful. "
                "I can help explain Vishal's projects, skills, "
                "education, and career goals."
            )

    # Clearly unrelated topics
    for word in OFF_TOPIC_KEYWORDS:
        if word in text:
            return (
                "That is outside my scope. "
                "I am a project explainer chatbot focused on "
                "Vishal's projects, technical skills, education, "
                "and career goals."
            )

    return None