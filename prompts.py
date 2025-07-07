def summarize_meeting_prompt(transcript: str) -> str:
    return (
        f"Summarize the following project meeting transcript, highlighting key decisions, "
        f"action items, discussion points, and any open questions. "
        f"Format it clearly with headings:\n\nTranscript:\n{transcript}\n\nSummary:"
    )


def draft_email_prompt(summary: str, recipient: str, project: str, purpose: str, actions: str) -> str:
    return (
        f"Draft a concise and professional email to {recipient} regarding the {project} project. "
        f"The purpose of this email is to {purpose}.\n\nSummary:\n{summary}\n\nAction Items:\n{actions}\n\nEmail:"
    )


def wbs_prompt(goal: str) -> str:
    return (
        f"Given the project goal: '{goal}', break it down into a detailed Work Breakdown Structure (WBS) "
        f"with estimated task durations and key deliverables. Organize by phases or major components."
    )


def risk_prompt(description: str, context: str = "") -> str:
    return (
        f"Given the project description: '{description}'. Additional context: '{context if context else 'None.'}'. "
        f"Identify 5-7 potential risks for this project and suggest concrete mitigation strategies for each. "
        f"Consider scope, budget, schedule, resources, and quality."
    )
