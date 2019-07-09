import subprocess
pl = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()
print(pl[0].decode('utf-8'))
