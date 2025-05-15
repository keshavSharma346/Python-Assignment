try:
    x = 10
    x.append(5)
except AttributeError as e:
    print("Attribute Error:", e)
