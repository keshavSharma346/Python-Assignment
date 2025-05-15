try:
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print("Key Error:", e)
