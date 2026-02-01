from google import genai
from google.genai import types

class GEMINI_API:
    def __init__(self, api_key, config_sol, config_exp):

        self.API_KEY = api_key
        self.client = genai.Client(api_key=self.API_KEY)
        self.config_solution = config_sol
        self.config_explain = config_exp
    
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
