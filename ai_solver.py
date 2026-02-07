from google import genai
from google.genai import types
import os
import json
from dotenv import load_dotenv

load_dotenv()

class AISolver:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = "gemini-2.5-flash"

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
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            
            return json.loads(response.text)
            
        except Exception as e:
            return {
                "analysis": f"API Error: {str(e)}", 
                "solutions": []
            }