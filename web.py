import subprocess
import time

subprocess.run("python3 -m http.server 8000 -b 10.60.36.71")
while True:
    print("Server now running ...")
    time.sleep(10)


