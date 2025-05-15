try:
    x = 5 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
except NameError:
    print("Caught NameError")
except Exception as e:
    print("Caught general exception:", e)
