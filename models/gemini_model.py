# models/gemini_model.py

import google.generativeai as genai
import os

GEMINI_API_KEY = "AIzaSyCoAKKfNiCzH16M1sAZyCHpjokd4dl3LZs"

genai.configure(api_key=GEMINI_API_KEY)

# def summarize_code_gemini(code_snippet, prompt_template):
#     """Generates a summary using Google's Gemini API."""
#     prompt = prompt_template.format(code=code_snippet)
#     model = genai.GenerativeModel("gemini-2.0-flash")
#     response = model.generate_content(prompt)
#     return response.text.strip()

# if __name__ == "__main__":
#     sample_code = "def multiply(a, b): return a * b"
#     print(summarize_code(sample_code))

def summarize_code_gemini(code_snippet, prompt_template):
    """Generates a summary using Google's Gemini API."""
    prompt = prompt_template.replace("{code}", code_snippet)  # Safely replace {code}
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

