import subprocess

term = subprocess.run("ssh tars@192.168.50.99")
term.check_returncode()