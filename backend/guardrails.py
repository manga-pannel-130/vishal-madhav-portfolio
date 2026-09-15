# backend/guardrails.py

import re


BLOCKED_PATTERNS = [
    r"\bpassword\b",
    r"\bapi[\s_-]?key\b",
    r"\bsecret\b",
    r"\btoken\b",
    r"\bcredit card\b",
    r"\bcard number\b",
    r"\bssn\b",
    r"\bsocial security\b",
]


OFF_TOPIC_PATTERNS = [
    r"\bpolitics\b",
    r"\bpolitician\b",
    r"\belection\b",
    r"\bweather\b",
    r"\bstock price\b",
    r"\bcrypto price\b",
]


def check_guardrails(message: str):
    """
    Returns:
        (allowed, response)

    If allowed is True, response is None.
    If allowed is False, response contains the safe response.
    """

    if not message or not message.strip():
        return False, "Ask me something about Vishal or one of the projects in the archive."

    text = message.lower().strip()

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text):
            return (
                False,
                "I can't provide private credentials, secrets, or sensitive personal information. "
                "I can talk about the projects and technical work documented in the archive."
            )

    for pattern in OFF_TOPIC_PATTERNS:
        if re.search(pattern, text):
            return (
                False,
                "I'm focused on Vishal's work and the projects in the archive. "
                "Ask me about a project, how something was built, or what Vishal worked on."
            )

    return True, None