try:
    import nonexistingmodule
except ModuleNotFoundError as e:
    print("Module Not Found Error:", e)
