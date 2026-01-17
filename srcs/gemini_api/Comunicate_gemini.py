from google import genai
from google.genai import types

class GEMINI_API:
    def __init__(self, api_key):

        self.API_KEY = api_key
        self.client = genai.Client(api_key=self.API_KEY)
        self.config_solution = "Your a expert of Python. You will resolve a python environment problems. When you receive a problem, you should reply solutions like 'Option 1 : python3 -m pip install google; pip upgrade google;'. You should show us 3 options. and do not descibe anything else without options."
        self.config_explain = "Your a expert of Python. You will resolve a python environment problems. When you receive a solution, you should explain solutions like 'Option 1 : it will remove something and install a' and each option should be describe in one sentence. and do not descibe anything else without options."
    
    def get_response(self, error_message):
        
        response_sol = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=error_message,
            config=types.GenerateContentConfig(
                system_instruction=self.config_solution
            ))
        
        sol = response_sol.text
        
        response_explain = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=sol,
            config=types.GenerateContentConfig(
                system_instruction=self.config_explain
            ))
        
        explain = response_explain.text
        
        return sol, explain
