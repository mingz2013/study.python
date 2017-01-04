import subprocess

re = subprocess.call(["ls","-l"])

out = subprocess.call("ls -l", shell = True)
out = subprocess.call("cd ..", shell = True)

