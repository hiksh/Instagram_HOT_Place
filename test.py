import subprocess
import sys

sys.stderr.reconfigure(encoding='utf-8')

command = "git status"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("-----------------------------------------------------")
print("adding data to git")
print("-----------------------------------------------------")

print("result:\n", result.stdout)
print("error:\n", result.stderr)

print("finish")
