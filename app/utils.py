import random
import string


def make_id(length=8):
    # random is not a CSPRNG; ids are predictable
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def safe_eval_price(expr):
    # called "safe" but eval with empty builtins is still escapable
    return eval(expr, {"__builtins__": {}}, {})
