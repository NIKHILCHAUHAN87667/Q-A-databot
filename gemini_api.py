import google.generativeai as genai
import os

def init_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file or as an environment variable.")
    genai.configure(api_key=api_key)
    # Replace "gemini-pro" with the correct model ID
    return genai.GenerativeModel("gemini-2.0-flash")

def get_email_template(prompt_file):
    with open(prompt_file, "r") as file:
        prompt = file.read()
    try:
        model = init_gemini()
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Failed to generate email template: {e}")
