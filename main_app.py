import streamlit as st
from db_utils import init_db
from health_fitness import fitness_tracker
from mental_wellness import mental_wellness
from event_reminder import birthday_reminder
from meeting_reminders import meeting_reminders
from project_deadlines import project_deadlines
from report_generator import report_generator

# Initialize database
init_db()

# Main Dashboard
st.title("🤖 AI-Powered Coach Dashboard")
choice = st.radio("Select Coaching Type:", ("Personal Coaching", "Professional Coaching"))

if choice == "Personal Coaching":
    st.subheader("📋 Personal Coaching Categories")
    option = st.selectbox("Choose a category", ["Select", "Health & Fitness", "Mental Wellness", "Birthdays/Anniversaries Reminder"])

    if option == "Health & Fitness":
        fitness_tracker()
    elif option == "Mental Wellness":
        mental_wellness()
    elif option == "Birthdays/Anniversaries Reminder":
        birthday_reminder()

elif choice == "Professional Coaching":
    st.subheader("📋 Professional Coaching Categories")
    option = st.selectbox("Choose a category", ["Select", "Meeting Reminders", "Project Deadlines", "PDF Reports"])

    if option == "Meeting Reminders":
        meeting_reminders()
    elif option == "Project Deadlines":
        project_deadlines()
    elif option == "PDF Reports":
        report_generator()
        project_deadlines()

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")