import streamlit as st
from fpdf import FPDF
import os

def generate_pdf_report(title, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align="C")
    pdf.multi_cell(0, 10, txt=content)
    
    filename = f"{title.replace(' ', '_')}.pdf"
    pdf.output(filename)
    return filename

def report_generator():
    st.subheader("📁 PDF Report Generator")
    
    if "report_generated" not in st.session_state:
        st.session_state.report_generated = False
        st.session_state.report_filename = ""

    with st.form("report_form"):
        title = st.text_input("Report Title")
        content = st.text_area("Report Content", height=300)
        submit = st.form_submit_button("Generate Report")

        if submit:
            if title and content:
                filename = generate_pdf_report(title, content)
                st.session_state.report_generated = True
                st.session_state.report_filename = filename
            else:
                st.warning("Please provide both title and content.")

    if st.session_state.report_generated:
        with open(st.session_state.report_filename, "rb") as f:
            st.download_button("📥 Download Report", f, file_name=st.session_state.report_filename)
        os.remove(st.session_state.report_filename)
        st.session_state.report_generated = False
