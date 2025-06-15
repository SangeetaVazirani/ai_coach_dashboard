import streamlit as st
import sqlite3

def init_meeting_db():
    conn = sqlite3.connect("meetings.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS meetings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        date TEXT,
                        time TEXT)""")
    conn.commit()
    conn.close()

def save_meeting(title, date, time):
    conn = sqlite3.connect("meetings.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO meetings (title, date, time) VALUES (?, ?, ?)", (title, date, time))
    conn.commit()
    conn.close()

def show_meetings():
    conn = sqlite3.connect("meetings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meetings ORDER BY date, time")
    rows = cursor.fetchall()
    conn.close()
    return rows

def meeting_reminders():
    init_meeting_db()

    with st.form("meeting_form"):
        title = st.text_input("Meeting Title")
        date = st.date_input("Meeting Date")
        time = st.time_input("Meeting Time")
        submit = st.form_submit_button("Save Meeting")
        if submit:
            save_meeting(title, date.strftime("%Y-%m-%d"), time.strftime("%H:%M"))
            st.success("Meeting saved successfully!")

    st.subheader("📅 Upcoming Meetings")
    meetings = show_meetings()
    for id, title, date, time in meetings:
        st.write(f"**{title}** — {date} at {time}")