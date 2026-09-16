# backend/guardrails.py

import re


BLOCKED_PATTERNS = [
    r"\bpassword\b",
    r"\bapi[\s_-]?key\b",
    r"\bsecret\b",
    r"\baccess[\s_-]?token\b",
    r"\bauth[\s_-]?token\b",
    r"\bprivate[\s_-]?key\b",
    r"\bcredit[\s_-]?card\b",
    r"\bcard[\s_-]?number\b",
    r"\bcvv\b",
    r"\bssn\b",
    r"\bsocial[\s_-]?security\b",
]

OFF_TOPIC_PATTERNS = [
    r"\bpolitics\b",
    r"\bpolitician\b",
    r"\belection\b",
    r"\bweather\b",
    r"\bstock[\s_-]?price\b",
    r"\bcrypto[\s_-]?price\b",
]


BLOCKED_RESPONSE = (
    "I can't provide private credentials, secrets, or sensitive "
    "personal information. I can talk about the projects and "
    "technical work documented in the archive."
)


OFF_TOPIC_RESPONSE = (
    "I'm focused on Vishal's work and the projects in the archive. "
    "Ask me about a project, how something was built, or what "
    "Vishal worked on."
)


EMPTY_RESPONSE = (
    "Ask me something about Vishal or one of the projects in the archive."
)


def check_guardrails(message: str):
    """
    Validate a user message before it reaches the LLM.

    Returns:
        (allowed, response)

    If allowed is True:
        response is None.

    If allowed is False:
        response contains the safe response to show the user.
    """

    if not isinstance(message, str):
        return False, EMPTY_RESPONSE

    message = message.strip()

    if not message:
        return False, EMPTY_RESPONSE

    text = message.lower()

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text):
            return False, BLOCKED_RESPONSE

    for pattern in OFF_TOPIC_PATTERNS:
        if re.search(pattern, text):
            return False, OFF_TOPIC_RESPONSE

    return True, None