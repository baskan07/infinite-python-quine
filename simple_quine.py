s = 's = %r\nwith open("clone.py", "w") as f:\n    f.write(s %% s)\nprint("I have written myself as clone.py")'
with open("clone.py", "w") as f:
    f.write(s % s)
print("I have written myself as clone.py")