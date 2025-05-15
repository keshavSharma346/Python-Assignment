try:
    with open("nofile.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("File Not Found Error:", e)
