# backend/knowledge.py


PROFILE = {
    "name": "Vishal Madhav",
    "role": "Computer Science Engineering Student",
    "direction": "BUILDING AI SYSTEMS",
    "tagline": "Figuring out how everything works, one build at a time.",
    "intro": (
        "I'm Vishal, a Computer Science Engineering student exploring "
        "AI systems by building things and figuring out how they work."
    ),
}


PROJECTS = {

    # =========================================================
    # PAST BUILDS
    # =========================================================

    "skillsense": {
        "number": "01",
        "title": "SkillSense",
        "category": "PAST BUILD",
        "ownership": "TEAM",
        "type": "Team Project",
        "status": "Completed",

        "short_description": (
            "An AI-driven skill assessment and career guidance platform."
        ),

        "why": (
            "SkillSense explored the problem of understanding a person's "
            "skills and helping connect those skills with suitable career "
            "directions."
        ),

        "overview": (
            "SkillSense is an AI-driven platform designed to assess users' "
            "skills and provide guidance for skill development and career growth."
        ),

        "my_contribution": (
            "I contributed to the Quiz Generation module. It generates "
            "skill-assessment quizzes based on topics selected by the user "
            "and supports different difficulty levels."
        ),

        "technical": (
            "The broader project used AI-driven components to support skill "
            "assessment and career guidance. My documented work was "
            "specifically focused on the quiz-generation part of that system."
        ),

        "challenge": (
            "One of the main things I worked through was making the quiz "
            "generation respond to the selected topic and difficulty rather "
            "than simply producing a fixed set of questions."
        ),

        "lesson": (
            "This project introduced me to the idea of breaking a larger "
            "AI application into individual components that solve specific "
            "parts of a workflow."
        ),

        "remember": (
            "I contributed to the Quiz Generation module of a team-built "
            "AI skill assessment platform."
        ),

        "technologies": [
            "Python",
            "Artificial Intelligence",
        ],

        "github": None,
        "live": None,
    },


    # =========================================================
    # CURRENT BUILDS
    # =========================================================

    "hiring-agent": {
        "number": "01",
        "title": "Hiring Agent",
        "category": "CURRENT BUILD",
        "ownership": "SOLO",
        "type": "Solo Project",
        "status": "Prototype",

        "short_description": (
            "An AI recruiter that evaluates candidates against job requirements."
        ),

        "why": (
            "While working on SkillSense, I encountered the broader problem "
            "of matching people to suitable roles. I wanted to explore that "
            "idea independently and build a smaller system around it."
        ),

        "overview": (
            "Hiring Agent takes a job description and candidate resumes and "
            "evaluates how well each candidate matches the role. It can score "
            "candidates, identify strengths and weaknesses, provide reasoning, "
            "generate interview questions, and rank multiple candidates."
        ),

        "my_contribution": (
            "I built this as a solo project. I worked on the application flow, "
            "candidate evaluation, matching logic, scoring, resume handling, "
            "and the interface used to review candidates."
        ),

        "technical": (
            "The application accepts job descriptions and resumes, extracts "
            "relevant information, compares candidate information with the "
            "requirements of the role, and produces an evaluation. The project "
            "also supports an AI-based evaluation path with a simpler fallback "
            "approach."
        ),

        "challenge": (
            "The interesting part was turning a fairly subjective problem — "
            "whether a candidate is suitable for a role — into something the "
            "system could evaluate in a structured way."
        ),

        "lesson": (
            "This project was my first step toward taking an idea I encountered "
            "inside a larger team project and independently turning it into "
            "a separate AI application."
        ),

        "remember": (
            "I took the role-matching idea I encountered in SkillSense and "
            "explored it independently as a standalone AI recruiter."
        ),

        "technologies": [
            "Python",
            "Artificial Intelligence",
            "Streamlit",
            "Resume Parsing",
        ],

        "github": "https://github.com/manga-pannel-130/Hiring-Agent",
        "live": None,
    },


    "recoverai": {
        "number": "02",
        "title": "RecoverAI",
        "category": "CURRENT BUILD",
        "ownership": "SOLO",
        "type": "Razorpay Buildathon",
        "status": "Refinement",

        "short_description": (
            "An AI-driven system for analysing failed payments and "
            "determining recovery actions."
        ),

        "why": (
            "I built RecoverAI specifically for the Razorpay Buildathon. "
            "Before starting the project, I knew very little about payment "
            "failures or payment recovery."
        ),

        "overview": (
            "RecoverAI is designed to analyse failed transactions, identify "
            "possible recovery paths, and process recovery actions intended "
            "to improve successful payment completion."
        ),

        "my_contribution": (
            "I built RecoverAI as a solo project. I worked across the system, "
            "including the AI component, backend, database, recovery workflow, "
            "transaction diagnostics, retry logic, and frontend."
        ),

        "technical": (
            "The system receives transaction information, analyses the failure, "
            "applies the documented recovery logic, and records the result. "
            "The project includes an AI-driven recovery component and retry "
            "logic. The archive does not currently document specific external "
            "payment-provider API integration details."
        ),

        "challenge": (
            "One of the most confusing parts for me was working through the "
            "database architecture and the transition between PostgreSQL and "
            "Prisma. Understanding how the application, ORM layer, and database "
            "fit together became part of the learning process."
        ),

        "lesson": (
            "RecoverAI taught me how to approach a problem I initially knew "
            "nothing about and gradually turn it into a working system. "
            "More importantly, it taught me how to structure an application "
            "when starting from an idea rather than from an existing "
            "implementation."
        ),

        "remember": (
            "I started with almost no knowledge of payment recovery and worked "
            "my way from the problem to a functioning AI-driven system."
        ),

        "weakness": (
            "The current frontend does not expose all the information produced "
            "by the AI system. It currently presents only the basic results, "
            "so improving how the reasoning and recovered information are "
            "visualised is one of the next areas of refinement."
        ),

        "technologies": [
            "React",
            "Node.js",
            "Express.js",
            "PostgreSQL",
            "Prisma",
            "Artificial Intelligence",
        ],

        "github": None,
        "live": None,
    },


    "had": {
        "number": "03",
        "title": "HAD",
        "category": "CURRENT BUILD",
        "ownership": "TEAM",
        "type": "Team Project",
        "status": "Prototype",

        "short_description": (
            "A prototype exploring workflow optimisation across CAD, "
            "FEA and topology optimisation."
        ),

        "why": (
            "This is a team project focused on exploring how the workflow "
            "around CAD design, FEA and topology optimisation could be "
            "streamlined and optimised."
        ),

        "overview": (
            "HAD is a prototype for a system intended to optimise parts of "
            "the workflow involved in building and evaluating CAD models, "
            "including FEA and topology optimisation."
        ),

        "my_contribution": (
            "I worked on the project as part of a team. The current version "
            "is a prototype, so my individual contribution is not yet "
            "documented in enough detail to describe specific implementation "
            "responsibilities."
        ),

        "technical": (
            "The prototype brings together stages of a CAD-oriented engineering "
            "workflow involving CAD modelling, finite element analysis and "
            "topology optimisation."
        ),

        "challenge": (
            "The main challenge is understanding how the individual stages "
            "of the engineering workflow can be connected into a more "
            "efficient overall process."
        ),

        "lesson": (
            "The project exposed me to a problem domain very different from "
            "my previous AI-focused applications and made me think about "
            "how complex engineering workflows can be represented as systems."
        ),

        "remember": (
            "A team prototype exploring how CAD, FEA and topology optimisation "
            "can be brought into a more efficient workflow."
        ),

        "technologies": [
            "CAD",
            "FEA",
            "Topology Optimisation",
        ],

        "github": None,
        "live": None,
    },


    "ai-soc-analyst": {
        "number": "04",
        "title": "AI SOC Analyst",
        "category": "CURRENT BUILD",
        "ownership": "SOLO",
        "type": "AI Lab Micro Project",
        "status": "Building",

        "short_description": (
            "An AI-assisted security operations project focused on "
            "exploring automated security analysis."
        ),

        "why": (
            "I wanted to explore how AI systems can be applied to security "
            "operations and how repetitive analysis tasks could be assisted "
            "through automation."
        ),

        "overview": (
            "AI SOC Analyst is a micro project I am currently building for "
            "the AI Lab. The project explores the idea of using AI to assist "
            "with security operations and analysis."
        ),

        "my_contribution": (
            "I am building the project as an individual micro project, "
            "working on the application flow and the AI-assisted analysis "
            "components."
        ),

        "technical": (
            "The project is currently under development. Its technical "
            "implementation and AI workflow are still being refined."
        ),

        "challenge": (
            "The main challenge is figuring out how to turn security data "
            "and analysis tasks into a workflow that an AI system can "
            "assist with in a useful and structured way."
        ),

        "lesson": (
            "This project is helping me explore the intersection of AI, "
            "automation and cybersecurity through a practical system."
        ),

        "remember": (
            "A current AI Lab micro project exploring AI-assisted "
            "security operations analysis."
        ),

        "technologies": [
            "Artificial Intelligence",
            "Cybersecurity",
        ],

        "github": None,
        "live": None,
    },


    "mealmate": {
        "number": "05",
        "title": "MealMate",
        "category": "CURRENT BUILD",
        "ownership": "SOLO",
        "type": "Application",
        "status": "Building",

        "short_description": (
            "A meal planning application for organising meals and "
            "discovering recipes based on available ingredients."
        ),

        "why": (
            "I built MealMate to explore how a practical application could "
            "help users plan meals and find suitable recipes without having "
            "to organise everything manually."
        ),

        "overview": (
            "MealMate is a web application that supports user accounts, "
            "meal planning and recipe recommendations based on ingredients. "
            "I am currently continuing to develop the project and explore "
            "additional features."
        ),

        "my_contribution": (
            "I built the application and worked across the frontend, backend, "
            "database integration, authentication and meal-planning workflow."
        ),

        "technical": (
            "The application uses a React frontend with a FastAPI backend "
            "and MySQL for user and application data. It integrates with "
            "the Spoonacular API for recipe and ingredient-related data."
        ),

        "challenge": (
            "One of the challenges was connecting the frontend, backend, "
            "database and external recipe API into a single workflow that "
            "could support authentication and meal planning."
        ),

        "lesson": (
            "MealMate helped me understand how the different parts of a "
            "full-stack application need to work together rather than "
            "treating the frontend and backend as separate pieces."
        ),

        "remember": (
            "A full-stack meal planning application built with React, "
            "FastAPI and MySQL, currently being expanded with additional features."
        ),

        "technologies": [
            "React",
            "FastAPI",
            "MySQL",
            "Spoonacular API",
        ],

        "github": None,
        "live": None,
    },
}


# =============================================================
# PROJECT GROUPS
# =============================================================

PAST_PROJECTS = [
    "skillsense",
]


CURRENT_PROJECTS = [
    "hiring-agent",
    "recoverai",
    "had",
    "ai-soc-analyst",
    "mealmate",
]


# =============================================================
# SKILLS
# =============================================================

SKILLS = [
    "Python",
    "C",
    "C++",
    "Java",
    "JavaScript",
    "React",
    "FastAPI",
    "Node.js",
    "Express.js",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Git",
    "GitHub",
    "Artificial Intelligence",
]


# =============================================================
# EDUCATION
# =============================================================

EDUCATION = (
    "I am a Computer Science Engineering student at "
    "Coimbatore Institute of Technology, pursuing a B.E. in "
    "Computer Science and Engineering."
)


# =============================================================
# CAREER DIRECTION
# =============================================================

CAREER_GOAL = (
    "I want to build AI systems. I'm interested in understanding how "
    "intelligent systems can be designed, connected to real problems, "
    "and turned into useful applications."
)


# =============================================================
# CURRENT WORK
# =============================================================

CURRENTLY_WORKING_ON = (
    "I'm currently building Hiring Agent, refining RecoverAI, working "
    "on the HAD team project, building the AI SOC Analyst micro project, "
    "and continuing development of MealMate. I'm also building this "
    "portfolio as an interactive archive of my work."
)