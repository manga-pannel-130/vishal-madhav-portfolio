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
from backend.persona import PERSONA


_llm_client = None


def get_llm():
    global _llm_client

    if _llm_client is None:
        _llm_client = LLMClient()

    return _llm_client


def build_knowledge_context():
    """
    Convert the structured archive into a single factual context block.

    This is the source material the LLM is allowed to use when answering
    questions about Vishal and his projects.
    """

    context = []

    context.append("=== PROFILE ===")
    context.append(f"Name: {PROFILE['name']}")
    context.append(f"Role: {PROFILE['role']}")
    context.append(f"Direction: {PROFILE['direction']}")
    context.append(f"Tagline: {PROFILE['tagline']}")
    context.append(f"Introduction: {PROFILE['intro']}")

    context.append("\n=== EDUCATION ===")
    context.append(EDUCATION)

    context.append("\n=== CAREER DIRECTION ===")
    context.append(CAREER_GOAL)

    context.append("\n=== CURRENTLY WORKING ON ===")
    context.append(CURRENTLY_WORKING_ON)

    context.append("\n=== SKILLS ===")
    context.append(", ".join(SKILLS))

    context.append("\n=== PROJECT STATUS ===")

    past_build_names = [
        PROJECTS[project_id]["title"]
        for project_id in PAST_PROJECTS
        if project_id in PROJECTS
    ]

    current_build_names = [
        PROJECTS[project_id]["title"]
        for project_id in CURRENT_PROJECTS
        if project_id in PROJECTS
    ]

    context.append(
        "Past builds: "
        + (", ".join(past_build_names) if past_build_names else "None")
    )

    context.append(
        "Current builds: "
        + (", ".join(current_build_names) if current_build_names else "None")
    )

    context.append("\n=== PROJECT ARCHIVE ===")

    for project_id, project in PROJECTS.items():

        context.append(f"\n--- PROJECT: {project['title']} ---")
        context.append(f"Project ID: {project_id}")
        context.append(f"Ownership: {project['ownership']}")
        context.append(f"Type: {project['type']}")
        context.append(f"Status: {project['status']}")

        context.append(f"Why it was built: {project['why']}")
        context.append(f"Overview: {project['overview']}")
        context.append(f"Personal contribution: {project['my_contribution']}")
        context.append(f"Technical information: {project['technical']}")
        context.append(f"Challenge: {project['challenge']}")
        context.append(f"Lesson: {project['lesson']}")
        context.append(f"Important takeaway: {project['remember']}")

        if "weakness" in project:
            context.append(
                f"Known limitation: {project['weakness']}"
            )

        context.append(
            "Technologies: "
            + ", ".join(project["technologies"])
        )

        if project.get("github"):
            context.append(
                f"GitHub: {project['github']}"
            )

        if project.get("live"):
            context.append(
                f"Live project: {project['live']}"
            )

    return "\n".join(context)


def build_system_prompt():
    """
    Build the complete system instruction.

    PERSONA defines behavior.
    ARCHIVE DATA defines factual knowledge.
    """

    knowledge_context = build_knowledge_context()

    return (
        PERSONA
        + "\n\n"
        + "=== ARCHIVE DATA ===\n"
        + knowledge_context
        + "\n\n"
        + "=== END ARCHIVE DATA ==="
    )


def get_response(
    user_message: str,
    conversation_history: list | None = None,
):
    """
    Generate an Archive response.

    Guardrails run before the LLM.
    Conversation history is treated only as conversational context,
    never as a source of factual information.
    """

    allowed, guardrail_response = check_guardrails(user_message)

    if not allowed:
        return guardrail_response

    system_prompt = build_system_prompt()

    safe_history = sanitize_conversation_history(
        conversation_history
    )

    try:
        llm = get_llm()

        response = llm.generate_response(
            system_prompt=system_prompt,
            user_message=user_message,
            conversation_history=safe_history,
        )

        return clean_response(response)

    except Exception as error:
        print(f"LLM error: {error}")

        return fallback_response(user_message)


def sanitize_conversation_history(
    conversation_history: list | None,
) -> list:
    """
    Validate conversation history received from the frontend.

    History is useful for conversational continuity, but it is NOT
    considered part of the archive knowledge base.

    Only normal user/assistant messages are accepted.
    """

    if not isinstance(conversation_history, list):
        return []

    safe_history = []

    for message in conversation_history[-10:]:

        if not isinstance(message, dict):
            continue

        role = message.get("role")
        content = message.get("content")

        if role not in {"user", "assistant"}:
            continue

        if not isinstance(content, str):
            continue

        content = content.strip()

        if not content:
            continue

        safe_history.append(
            {
                "role": role,
                "content": content[:4000],
            }
        )

    return safe_history


def clean_response(response: str) -> str:
    """
    Basic output cleanup.

    The persona already controls formatting, but this prevents accidental
    whitespace and empty responses from reaching the UI.
    """

    if not isinstance(response, str):
        return "I couldn't generate a response right now."

    response = response.strip()

    if not response:
        return "I couldn't generate a response right now."

    return response


def fallback_response(user_message: str):
    """
    Conservative fallback responses.

    These responses intentionally contain only information explicitly
    documented in the archive.
    """

    text = user_message.lower().strip()

    if "skillsense" in text:
        return (
            "SkillSense was a team project. My documented contribution "
            "was the Quiz Generation module, which generates "
            "skill-assessment quizzes based on selected topics and "
            "difficulty levels."
        )

    if "hiring" in text or "recruiter" in text:
        return (
            "Hiring Agent is a solo project where I explored AI-based "
            "candidate evaluation against job requirements. It takes "
            "job descriptions and resumes and produces structured "
            "candidate evaluations."
        )

    if "recoverai" in text or "recover ai" in text or "recover" in text:
        return (
            "RecoverAI is a solo Razorpay Buildathon project focused on "
            "analysing failed transactions and determining recovery "
            "actions. The current archive documents the recovery workflow "
            "and retry logic, but not specific external payment API "
            "integration details."
        )

    if "had" in text:
        return (
            "HAD is a team prototype exploring workflow optimisation "
            "across CAD, FEA and topology optimisation."
        )

    if "soc" in text or "security analyst" in text:
        return (
            "AI SOC Analyst is a current AI Lab micro project exploring "
            "AI-assisted security operations and analysis."
        )

    if "mealmate" in text or "meal mate" in text:
        return (
            "MealMate is a full-stack meal planning application built "
            "with React, FastAPI and MySQL. It uses the Spoonacular API "
            "for recipe and ingredient-related data."
        )

    if (
        "current" in text
        or "currently" in text
        or "working on" in text
        or "building" in text
    ):
        return (
            "I'm currently working on Hiring Agent, refining RecoverAI, "
            "working on the HAD team project, building the AI SOC Analyst "
            "micro project, and continuing development of MealMate."
        )

    if "who are you" in text or "about" in text:
        return (
            "I'm the AI project explainer inside Vishal's portfolio. "
            "I represent the documented project archive and can talk "
            "about his projects, contributions, technical work and "
            "what he learned."
        )

    return (
        "I'm focused on the projects and technical work documented "
        "in the archive. You can ask me about SkillSense, Hiring Agent, "
        "RecoverAI, HAD, AI SOC Analyst or MealMate."
    )