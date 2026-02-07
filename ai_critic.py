# import anthropic
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

# class AICritic:
#     def __init__(self):
#         self.client = anthropic.Anthropic(
#             api_key=os.getenv("ANTHROPIC_API_KEY")
#         )

#     def verify_safety(self, command):
#         # Checking Sequence
#         prompt = f"""
#         You are a Linux Security Auditor.
#         Review this command for safety:
        
#         Command: `{command}`
        
#         Risk Rules:
#         1. 'rm -rf', 'mkfs', 'dd', '> /dev/sda' are CRITICAL.
#         2. Global install (sudo pip) is WARNING.
#         3. Standard pip/apt install is SAFE.
        
#         Output JSON ONLY:
#         {{
#             "is_safe": true or false,
#             "risk_level": "LOW" or "MEDIUM" or "HIGH",
#             "warning_message": "Reason if unsafe, else empty string"
#         }}
#         """

#         try:
#             message = self.client.messages.create(
#                 model="claude-3-5-sonnet-20240620",
#                 max_tokens=200,
#                 messages=[{"role": "user", "content": prompt}]
#             )
            
#             # Parsing the response
#             response_text = message.content[0].text
#             return json.loads(response_text)
            
#         except Exception as e:
#             # if api occurs error
#             return {"is_safe": False, "risk_level": "UNKNOWN", "warning_message": "Verification Failed"}

class AICritic:
    def __init__(self):
        # .env에서 OPENAI_API_KEY를 자동으로 읽어옵니다.
        self.client = OpenAI() 

    def verify_safety(self, command):
        prompt = f"""
        You are a Linux Security Auditor.
        Review this command for safety.
        
        Command: `{command}`
        
        Risk Rules:
        1. 'rm -rf', 'mkfs', 'dd', '> /dev/sda' are CRITICAL.
        2. Global install (sudo pip) is WARNING.
        3. Standard pip/apt install is SAFE.
        
        Output JSON ONLY:
        {{
            "is_safe": true or false,
            "risk_level": "LOW" or "MEDIUM" or "HIGH",
            "warning_message": "Reason if unsafe, else empty string"
        }}
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful security assistant. Output in JSON."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}, # JSON 강제 모드 (핵심!)
                max_tokens=200,
                temperature=0
            )
            

            content = response.choices[0].message.content
            return json.loads(content)
            
        except Exception as e:
            return {
                "is_safe": False, 
                "risk_level": "UNKNOWN", 
                "warning_message": f"Verification Failed: {str(e)}"
            }