

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_bool(b):
    if b == "True": return True
    else: return False


