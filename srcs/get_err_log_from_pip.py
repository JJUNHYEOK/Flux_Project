import os
import subprocess
import sys

from dotenv import load_dotenv
from gemini_api import Comunicate_gemini

CONFIG_SOLUTION_PIP = "Your a expert of Python. You will resolve a python environment problems. When you receive a problem, you should reply solutions like 'Option 1 : python3 -m pip install google; pip upgrade google;'. You should show us 3 options. and do not descibe anything else without options."
CONFIG_EXPLANATION_PIP = "Your a expert of Python. You will resolve a python environment problems. When you receive a solution, you should explain solutions like 'Option 1 : it will remove something and install a' and each option should be describe in one sentence. and do not descibe anything else without options."

CONFIG_SOLUTION_PKG = "Your a expert of {}. You will resolve a {} environment problems like apt. When you receive a problem, you should reply solutions like 'Option 1 : {} install python-dev; {} install build-essentials;'. You should show us 3 options. and do not descibe anything else without options."
CONFIG_EXPLANATION_PKG = "Your a expert of {}. You will resolve a {} environment problems like apt. When you receive a solution, you should explain solutions like 'Option 1 : it will remove something and install a' and each option should be describe in one sentence. and do not descibe anything else without options."

PKG_NAME_DICT = {'Ubuntu':'apt'}


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

def get_env_from_linux():

    linux_name = None
    version = None
    with open('/etc/os-release', 'r') as f:
        linux_name = f.readline().strip().split(sep='=')[1]
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        version = f.readline().strip().split(sep='=')[1]

    return linux_name[1:-1], version[1:-1]

def main():

    # test_case = "python3 -m pip install Pillow==9.0.0"
    # cmd = test_case.split()

    cmd = [sys.argv[i] for i in range(1, len(sys.argv))]

    load_dotenv()
    API_KEY = os.environ['GEMINI_API_KEY']

    exe_result = subprocess.run(cmd, capture_output=True, text=True)
    err_message = exe_result.stderr

    if err_message:
        print(err_message)

        gemini = None
        if 'pip' in cmd:
            gemini = Comunicate_gemini.GEMINI_API(API_KEY, CONFIG_SOLUTION_PIP, CONFIG_EXPLANATION_PIP)
        elif 'apt' in cmd:
            linux_name, version = get_env_from_linux()

            gemini = Comunicate_gemini.GEMINI_API(API_KEY, CONFIG_SOLUTION_PKG.format(linux_name + ' ' + version, 
                                                                                      linux_name + ' ' + version, 
                                                                                      PKG_NAME_DICT[linux_name],
                                                                                      PKG_NAME_DICT[linux_name]), 
                                                                                      CONFIG_EXPLANATION_PKG.format(linux_name + ' ' + version,
                                                                                                                    linux_name + ' ' + version))

        sol, explain = gemini.get_response(err_message)

        solutions = parse_gen_sol(sol)
        explains = parse_gen_ex(explain)

        for i in range(3):
            print(f'Option {i} :', solutions[i])
            print('          ', explains[i])
        print(f'Option {3} : exit AI Solver')

        selected_option = int(input('Select an option to solve this problem : '))
        if selected_option < 3:
            os.system(solutions[selected_option])

    



if __name__ == '__main__':
    main()