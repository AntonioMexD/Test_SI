#filename="lab03.txt"
filename="lab02.txt"
with open(filename) as f:
    contents = f.read()

contents = contents.splitlines()
height = len(contents)
width = max(len(line) for line in contents)

print(contents)

