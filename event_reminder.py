import streamlit as st
from db_utils import save_event

def birthday_reminder():
    with st.form("event_form"):
        event_date = st.date_input("Select date of event")
        name = st.text_input("Person's Name")
        event_type = st.selectbox("Type of Event", ["Birthday", "Anniversary"])
        reminder_minutes = st.slider("Reminder before event (in minutes)", 0, 1440, 60)
        submit = st.form_submit_button("Save Event")

        if submit:
            save_event(event_date.strftime("%Y-%m-%d"), name, event_type, reminder_minutes)
            st.success(f"{event_type} for {name} saved successfully!")