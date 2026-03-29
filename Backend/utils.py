import google.generativeai as genai
import os
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_content(content_type, topic, tone, audience):
    prompt = f"""
    Create a {content_type} on "{topic}"
    Tone: {tone}
    Audience: {audience}

    Include:
    - Hook
    - Main content
    - Ending
    """

    response = model.generate_content(prompt)
    return response.text

def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_path = "output.pdf"
    pdf.output(file_path)

    return file_path