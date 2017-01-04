import subprocess

child = subprocess.Popen(["ping", "-c", "5", "www.google.com"])
print("parent process")

