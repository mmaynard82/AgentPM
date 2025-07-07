from gemini_api import call_gemini_api
from prompts import summarize_meeting_prompt, draft_email_prompt, wbs_prompt, risk_prompt
from utils import save_to_file


def main():
    print("""
    ---------------------------------------
        Gemini Project Management Copilot  
    ---------------------------------------
    """)

    while True:
        print("\nChoose an action:")
        print("1. Summarize Project Meeting Transcript")
        print("2. Draft Project-Related Email")
        print("3. Generate Work Breakdown Structure (WBS)")
        print("4. Identify Project Risks & Mitigation")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\nEnter the project meeting transcript (type 'END' on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'END':
                    break
                lines.append(line)
            transcript = "\n".join(lines)
            prompt = summarize_meeting_prompt(transcript)
            print("\nSummarizing meeting...")
            summary = call_gemini_api(prompt)
            print("\n--- Meeting Summary ---")
            print(summary)
            save_to_file("summary.txt", summary)

        elif choice == '2':
            recipient = input("Recipient Name: ")
            project = input("Project Name: ")
            purpose = input("Purpose: ")
            summary = input("Summary: ")
            actions = input("Action Items: ")
            prompt = draft_email_prompt(summary, recipient, project, purpose, actions)
            print("\nDrafting email...")
            email = call_gemini_api(prompt)
            print("\n--- Drafted Email ---")
            print(email)

        elif choice == '3':
            goal = input("Enter Project Goal: ")
            prompt = wbs_prompt(goal)
            print("\nGenerating WBS...")
            wbs = call_gemini_api(prompt)
            print("\n--- WBS ---")
            print(wbs)

        elif choice == '4':
            description = input("Project Description: ")
            context = input("Context (optional): ")
            prompt = risk_prompt(description, context)
            print("\nIdentifying risks...")
            risks = call_gemini_api(prompt)
            print("\n--- Risks ---")
            print(risks)

        elif choice == '5':
            print("Exiting Project Management Copilot. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()





