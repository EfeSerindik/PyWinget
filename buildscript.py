import os
import subprocess
script_name = "main.py"
exe_name = os.path.splitext(script_name)[0] + ".exe"
output_dir = "build"
os.makedirs(output_dir, exist_ok=True)
pyinstaller_cmd = [
    "pyinstaller",
    "--onefile", 
    "--distpath", output_dir, 
    script_name
] 
subprocess.run(pyinstaller_cmd)
print(f"{exe_name} is created in {output_dir}")
