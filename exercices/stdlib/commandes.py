import subprocess
p1 = subprocess.Popen(["ps","aux"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "java"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output, error = p2.communicate()
print(output)