import os

i = 0
while os.path.exists(f"clone_{i}.py"):
    i += 1

filename = f"clone_{i}.py"
s = 'import os\n\ni = %d\nwhile os.path.exists(f"clone_{i}.py"):\n    i += 1\n\nfilename = f"clone_{i}.py"\ns = %r\nwith open(filename, "w") as f:\n    f.write(s %% (i, s))\nprint(f"I have written a clone of myself as {filename}")'
with open(filename, "w") as f:
    f.write(s % (i, s))
print(f"I have written a clone of myself as {filename}")