def add_five(num):
    return num + 5


def greet(name):
    return f"Hello, {name}!"


def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"
    
print(check_codeword("horse"))


def report_length(str):
    length = len(str)
    return f"This string was {length} characters long."
