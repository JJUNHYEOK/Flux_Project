import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

class AISolver:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        # Choose the faster model
        self.model = genai.GenerativeModel('gemini-1.5-flash') 

    def generate_solution(self, context, error_log):
        prompt = f"""
        You are a DevOps Expert. Solve this Python environment error.
        
        [Context]
        {context}
        
        [Error Log]
        {error_log}
        
        [Task]
        Provide 3 solutions in STRICT JSON format.
        Schema:
        {{
            "analysis": "Root cause summary",
            "solutions": [
                {{ "id": 1, "command": "pip install ...", "explanation": "..." }},
                {{ "id": 2, "command": "...", "explanation": "..." }}
            ]
        }}
        NO MARKDOWN. ONLY JSON.
        """
        
        try:
            response = self.model.generate_content(prompt)
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_text)
        except Exception as e:
            return {"analysis": f"Solver Error: {str(e)}", "solutions": []}