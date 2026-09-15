# backend/chatbot.py

from backend.knowledge import (
    PROFILE,
    PROJECTS,
    PAST_PROJECTS,
    CURRENT_PROJECTS,
    SKILLS,
    EDUCATION,
    CAREER_GOAL,
    CURRENTLY_WORKING_ON,
)

from backend.guardrails import check_guardrails
from backend.llm import LLMClient


_llm_client = None


def get_llm():
    global _llm_client

    if _llm_client is None:
        _llm_client = LLMClient()

    return _llm_client


def build_knowledge_context():
    context = []

    context.append("PROFILE")
    context.append(f"Name: {PROFILE['name']}")
    context.append(f"Role: {PROFILE['role']}")
    context.append(f"Direction: {PROFILE['direction']}")
    context.append(f"Tagline: {PROFILE['tagline']}")
    context.append(f"Introduction: {PROFILE['intro']}")

    context.append("\nEDUCATION")
    context.append(EDUCATION)

    context.append("\nCAREER DIRECTION")
    context.append(CAREER_GOAL)

    context.append("\nCURRENTLY WORKING ON")
    context.append(CURRENTLY_WORKING_ON)

    context.append("\nSKILLS")
    context.append(", ".join(SKILLS))

    context.append("\nPROJECTS")

    for project_id, project in PROJECTS.items():

        context.append(f"\n--- {project['title']} ---")
        context.append(f"Ownership: {project['ownership']}")
        context.append(f"Type: {project['type']}")
        context.append(f"Status: {project['status']}")
        context.append(f"Why: {project['why']}")
        context.append(f"Overview: {project['overview']}")
        context.append(f"My contribution: {project['my_contribution']}")
        context.append(f"Technical overview: {project['technical']}")
        context.append(f"Challenge: {project['challenge']}")
        context.append(f"Lesson: {project['lesson']}")
        context.append(f"Important takeaway: {project['remember']}")

        if "weakness" in project:
            context.append(f"Known limitation: {project['weakness']}")

        context.append(
            f"Technologies: {', '.join(project['technologies'])}"
        )

    return "\n".join(context)


SYSTEM_PROMPT = """
You are "Ask the Archive", the AI assistant inside Vishal Madhav's
personal portfolio website.

Your job is to talk about Vishal, his projects, his learning process,
and his documented technical work.

PERSONALITY:
- Casual
- Conversational
- Curious
- Direct
- Human
- Not corporate
- Not overly enthusiastic
- Do not sound like a generic AI assistant

VOICE:
Speak about Vishal in first person because the assistant represents
Vishal's own project archive.

For example:
"I built RecoverAI for the Razorpay Buildathon."
"I worked on the Quiz Generation module."
"I started RecoverAI knowing almost nothing about payment recovery."

Do not repeatedly say "Vishal did..." when first person makes more sense.

IMPORTANT:
The supplied project context is the source of truth.

Never invent:
- technologies
- features
- achievements
- responsibilities
- metrics
- users
- deployments
- certifications
- technical architecture
- project outcomes

If something is not documented, say that it isn't currently documented
in the archive.

If the user asks for something unknown, briefly say so and redirect toward
what is documented.

PROJECT OWNERSHIP:
Be extremely accurate about TEAM vs SOLO projects.

SkillSense is a TEAM project.
HAD is a TEAM project.
Hiring Agent is a SOLO project.
RecoverAI is a SOLO project.

Never imply that Vishal personally built the entire SkillSense system.
His documented contribution there is the Quiz Generation module.

Never imply that Vishal personally built the entire HAD system.
It is a team prototype.

RECOVERAI:
Be honest that Vishal started with very little knowledge of payment
recovery and learned while building the system.

Do not portray him as a payment systems expert.

FORMATTING:
The frontend currently displays responses as plain text.

Therefore:
- Do not use Markdown.
- Do not use headings with #.
- Do not use **bold**.
- Do not use bullet characters unless necessary.
- Use short paragraphs.
- Keep most answers between 2 and 5 short paragraphs.

When explaining a project, naturally cover:
1. Why it was built
2. What it does
3. Vishal's contribution
4. How it works at a high level
5. What was learned or challenging

Do not force all five points into every response.

If the user asks a simple question, give a simple answer.
"""


def get_response(
    user_message: str,
    conversation_history: list | None = None,
):

    allowed, guardrail_response = check_guardrails(user_message)

    if not allowed:
        return guardrail_response

    knowledge_context = build_knowledge_context()

    system_prompt = (
        SYSTEM_PROMPT
        + "\n\nARCHIVE DATA:\n"
        + knowledge_context
    )

    try:
        llm = get_llm()

        return llm.generate_response(
            system_prompt=system_prompt,
            user_message=user_message,
            conversation_history=conversation_history,
        )

    except Exception as error:
        print(f"LLM error: {error}")

        return fallback_response(user_message)


def fallback_response(user_message: str):

    text = user_message.lower()

    if "skillsense" in text:
        return (
            "SkillSense was a team project. I specifically worked on the "
            "Quiz Generation module, which generated skill-assessment "
            "quizzes based on selected topics and difficulty levels."
        )

    if "hiring" in text or "recruiter" in text:
        return (
            "Hiring Agent was my solo exploration of the role-matching idea "
            "I encountered while working on SkillSense. It evaluates resumes "
            "against job requirements and produces candidate evaluations."
        )

    if "recoverai" in text or "recover" in text:
        return (
            "I built RecoverAI for the Razorpay Buildathon. I started with "
            "very little knowledge of payment recovery and worked my way "
            "toward a functioning AI-driven recovery system."
        )

    if "had" in text:
        return (
            "HAD is a team prototype exploring workflow optimisation across "
            "CAD, FEA and topology optimisation."
        )

    if "who are you" in text or "about" in text:
        return (
            "I'm Ask the Archive. I can talk about Vishal's projects, "
            "how they were built, what he contributed, and what he learned."
        )

    return (
        "I'm focused on Vishal's projects and the work documented in the "
        "archive. Try asking me about SkillSense, Hiring Agent, RecoverAI, "
        "or HAD."
    )