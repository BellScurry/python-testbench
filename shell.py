import subprocess

p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
q = subprocess.Popen('cat shell.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in p.stdout.readlines():
    print(line.rstrip().decode('ascii'))

for line in q.stdout.readlines():
    print(line.rstrip().decode('ascii'))

retval = p.wait()
