from google import genai
from google.genai import types
import os
import json
from dotenv import load_dotenv

load_dotenv()

class AISolver:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = "gemini-3-flash-preview"

    def generate_solution(self, context, error_log):
        # 프롬프트는 그대로 두셔도 됩니다.
        prompt = f"""
        You are a DevOps Expert. Solve this Python environment error.
        
        [Context]
        {context}
        
        [Error Log]
        {error_log}
        
        [Task]
        Provide 3 solutions in STRICT JSON format.
        IMPORTANT: The output must be a JSON Object containing 'analysis' and 'solutions'.
        
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
            
            data = json.loads(response.text)

            if isinstance(data, list):
                return {
                    "analysis": "Analysis generated directly from solutions.",
                    "solutions": data
                }
                
            return data
            
        except Exception as e:
     
            return {
                "analysis": f"AI Parsing Error: {str(e)}", 
                "solutions": []
            }