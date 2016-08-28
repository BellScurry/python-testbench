import subprocess

p1 = subprocess.Popen('cat shell.py', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
p2 = subprocess.Popen('ls', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
p3 = subprocess.Popen('ls | xargs echo', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

for line in p1.stdout.readlines():
    print(line.rstrip().decode('ascii'))

for line in p2.stdout.readlines():
    print(line.rstrip().decode('ascii'))

for line in p3.stdout.readlines():
    print(line.rstrip().decode('ascii'))

retval = p1.wait()
