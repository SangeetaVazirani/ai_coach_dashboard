import streamlit as st
import sqlite3

def init_project_db():
    conn = sqlite3.connect("projects.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        deadline TEXT,
                        status TEXT)""")
    conn.commit()
    conn.close()

def save_project(name, deadline, status):
    conn = sqlite3.connect("projects.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, deadline, status) VALUES (?, ?, ?)", (name, deadline, status))
    conn.commit()
    conn.close()

def show_projects():
    conn = sqlite3.connect("projects.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects ORDER BY deadline")
    rows = cursor.fetchall()
    conn.close()
    return rows

def project_deadlines():
    init_project_db()

    with st.form("project_form"):
        name = st.text_input("Project Name")
        deadline = st.date_input("Deadline")
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
        submit = st.form_submit_button("Save Project")
        if submit:
            save_project(name, deadline.strftime("%Y-%m-%d"), status)
            st.success("Project saved successfully!")

    st.subheader("📊 Project Deadlines")
    projects = show_projects()
    for id, name, deadline, status in projects:
        st.write(f"**{name}** — Due by {deadline} | Status: {status}")