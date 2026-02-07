# mypackage/greeting.py

def say_hello(name):
    return f"Hello {name}"

def say_bye(name):
    return f"Bye {name}"

if __name__ == "__main__":
    print("This is excuted when running strings.py directly")
else:
    print("This is excuted when strings.py is imported as a module")