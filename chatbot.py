# chatbot.py

from knowledge import (
    PROFILE,
    PROJECTS,
    SKILLS,
    EDUCATION,
    CAREER_GOAL,
    CURRENTLY_WORKING_ON
)

from guardrails import check_guardrails


def apply_persona(response):

    return (
        "Hi! I'm Vishal's Project Explainer.\n\n"
        + response
        + "\n\n"
        "You can ask me about any of Vishal's projects, "
        "his contribution, technologies used, skills, "
        "education, or career goals."
    )


def project_response(project):

    response = f"### {project['title']}\n\n"

    response += f"{project['detailed_description']}\n\n"

    if "type" in project:
        response += f"Project Type: {project['type']}\n"

    if "team" in project:
        response += f"Team: {project['team']}\n"

    if "event" in project:
        response += f"Event: {project['event']}\n"

    if "status" in project:
        response += f"Status: {project['status']}\n"

    response += (
        f"\nMy Contribution:\n"
        f"{project['my_contribution']}\n"
    )

    if "technologies" in project:
        technologies = ", ".join(project["technologies"])

        response += (
            f"\nTechnologies:\n"
            f"{technologies}\n"
        )

    return apply_persona(response)


def get_all_projects():

    response = "Here are the main projects I can explain:\n\n"

    for project in PROJECTS.values():
        response += (
            f"• {project['title']} — "
            f"{project['description']}\n"
        )

    return apply_persona(response)


def get_skills():

    skills = ", ".join(SKILLS)

    return apply_persona(
        f"My main technical skills include:\n\n{skills}"
    )


def get_response(user_input):

    if not user_input:
        return apply_persona(
            "Please ask me something about Vishal's projects "
            "or technical background."
        )

    # -----------------------------------------
    # Guardrails
    # -----------------------------------------

    blocked_response = check_guardrails(user_input)

    if blocked_response:
        return blocked_response

    text = user_input.lower().strip()

    # -----------------------------------------
    # Greetings
    # -----------------------------------------

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if text in greetings:
        return apply_persona(
            "Hello! I can explain Vishal's projects, "
            "his contributions, technologies, skills, "
            "education, and career goals."
        )

    # -----------------------------------------
    # Project Overview
    # -----------------------------------------

    project_words = [
        "projects",
        "project",
        "portfolio",
        "applications",
        "apps"
    ]

    if any(word in text for word in project_words):

        # If a specific project is mentioned,
        # the specific project logic below will handle it.
        specific_project = False

        for key, project in PROJECTS.items():

            if (
                key in text
                or project["title"].lower() in text
            ):
                specific_project = True
                break

        if not specific_project:
            return get_all_projects()

    # -----------------------------------------
    # Individual Projects
    # -----------------------------------------

    for key, project in PROJECTS.items():

        project_name = project["title"].lower()

        if key in text or project_name in text:

            return project_response(project)

    # -----------------------------------------
    # Skills
    # -----------------------------------------

    if (
        "skills" in text
        or "skill" in text
        or "technologies" in text
        or "technology" in text
        or "tech stack" in text
        or "programming languages" in text
    ):
        return get_skills()

    # -----------------------------------------
    # Education
    # -----------------------------------------

    if (
        "education" in text
        or "college" in text
        or "university" in text
        or "study" in text
        or "studying" in text
        or "degree" in text
    ):
        return apply_persona(EDUCATION)

    # -----------------------------------------
    # Career
    # -----------------------------------------

    if (
        "career" in text
        or "goal" in text
        or "future" in text
        or "aspiration" in text
        or "become" in text
    ):
        return apply_persona(CAREER_GOAL)

    # -----------------------------------------
    # Current Work
    # -----------------------------------------

    if (
        "currently working" in text
        or "working on" in text
        or "current project" in text
        or "now" in text
    ):
        return apply_persona(CURRENTLY_WORKING_ON)

    # -----------------------------------------
    # About Vishal
    # -----------------------------------------

    if (
        "about vishal" in text
        or "who is vishal" in text
        or "about you" in text
        or "who are you" in text
    ):
        return apply_persona(
            f"{PROFILE['name']} is a {PROFILE['role']} "
            f"interested in Artificial Intelligence, "
            f"Machine Learning, Problem Solving, and "
            f"Full Stack Development."
        )

    # -----------------------------------------
    # Fallback
    # -----------------------------------------

    return apply_persona(
        "I can explain the following:\n\n"
        "• Vishal's projects\n"
        "• Individual project contributions\n"
        "• Technologies used in each project\n"
        "• Technical skills\n"
        "• Education\n"
        "• Career goals\n\n"
        "Try asking something like "
        "\"Tell me about RecoverAI\" or "
        "\"What did Vishal contribute to SkillSense?\""
    )