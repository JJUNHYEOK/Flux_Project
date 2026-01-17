import os
import subprocess
import sys

from dotenv import load_dotenv
from gemini_api import Comunicate_gemini

def parse_gen_sol(solution):
    solution_options = solution.split(sep='\n')
    
    options = []
    for i in range(3):
        options.append(solution_options[i][10:])

    return options

def parse_gen_ex(solution):
    solution_options = solution.split(sep='\n')
    
    options = []
    for i in range(3):
        options.append(solution_options[i][10:])

    return options

def main():

    test_case = "python3 -m pip install Pillow==9.0.0"
    cmd = test_case.split()

    load_dotenv()
    API_KEY = os.environ['GEMINI_API_KEY']

    exe_result = subprocess.run(cmd, capture_output=True, text=True)
    err_message = exe_result.stderr

    if err_message:
        print(err_message)


        gemini = Comunicate_gemini.GEMINI_API(API_KEY)
        sol, explain = gemini.get_response(err_message)

        solutions = parse_gen_sol(sol)
        explains = parse_gen_ex(explain)

        for i in range(3):
            print(f'Option {i} :', solutions[i])
            print('          ', explains[i])

        selected_option = int(input('Select an option to solve this problem : '))
        os.system(solutions[selected_option])



if __name__ == '__main__':
    main()