import platform
import sys
import subprocess
import os

class SystemScanner:
    def get_context(self):
        # OS Information
        os_info = f"{platform.system()} {platform.release()} ({platform.version()})"
        
        # Python Information
        py_ver = sys.version.split()[0]
        
        # Check the Virtual Environment
        # if sys.prefix != sys.base_prefix -> Virtual Env
        is_venv = (sys.prefix != sys.base_prefix)
        venv_path = sys.prefix if is_venv else "None"

        # Summarize installed packages
        try:
            pip_freeze = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], text=True)
            # head -n 20
            pip_list = "\n".join(pip_freeze.split('\n')[:20]) + "\n...(truncated)"
        except:
            pip_list = "Could not fetch pip list"

        context_str = f"""
[System Context]
- OS: {os_info}
- Python Version: {py_ver}
- Virtual Env Active: {is_venv} (Path: {venv_path})
- Key Installed Packages:
{pip_list}
"""
        return context_str, is_venv

# test
if __name__ == "__main__":
    scanner = SystemScanner()
    print(scanner.get_context()[0])