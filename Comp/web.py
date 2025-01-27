import subprocess
import time

subprocess.run("python3 -m http.server 8000 -b 192.168.222.76")
while True:
    print("Server now running ...")
    time.sleep(10)


