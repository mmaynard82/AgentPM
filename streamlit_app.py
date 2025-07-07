import streamlit as st
import google.generativeai as genai
import os
from gemini_api import call_gemini_api
from prompts import summarize_meeting_prompt, draft_email_prompt, wbs_prompt, risk_prompt

api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")



st.title("🤖 Project Management Copilot")

choice = st.selectbox("What would you like to do?", [
    "Summarize Meeting",
    "Draft Email",
    "Generate WBS",
    "Identify Risks"
])

if choice == "Summarize Meeting":
    transcript = st.text_area("Paste transcript")
    if st.button("Summarize"):
        summary = call_gemini_api(summarize_meeting_prompt(transcript))
        st.subheader("Summary")
        st.write(summary)

elif choice == "Draft Email":
    recipient = st.text_input("Recipient")
    project = st.text_input("Project")
    purpose = st.text_input("Purpose")
    summary = st.text_area("Summary")
    actions = st.text_area("Actions")
    if st.button("Draft Email"):
        email = call_gemini_api(draft_email_prompt(summary, recipient, project, purpose, actions))
        st.subheader("Email")
        st.write(email)

elif choice == "Generate WBS":
    goal = st.text_input("Project Goal")
    if st.button("Generate"):
        wbs = call_gemini_api(wbs_prompt(goal))
        st.subheader("WBS")
        st.write(wbs)

elif choice == "Identify Risks":
    description = st.text_input("Project Description")
    context = st.text_input("Context")
    if st.button("Identify Risks"):
        risks = call_gemini_api(risk_prompt(description, context))
        st.subheader("Risks")
        st.write(risks)

