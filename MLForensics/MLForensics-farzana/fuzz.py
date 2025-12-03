import random
import string
import traceback


# 5 simple target functions

def safe_div(a, b):
    return a / b


def to_int(x):
    return int(x)


def concat_strings(a, b):
    return a + b


def list_index(lst, idx):
    return lst[idx]


def sqrt_like(x):
    if x < 0:
        raise ValueError("negative not allowed")
    return x ** 0.5


TARGETS = [safe_div, to_int, concat_strings, list_index, sqrt_like]



NAUGHTY_STRINGS = [
    "", "0", "NaN", "null", "DROP TABLE", "∞", "\x00", "☃",
]

def rand_number():
    return random.choice([
        random.randint(-10, 10),
        random.uniform(-10, 10),
        0,
    ])

def rand_string():
    if random.random() < 0.5:
        return random.choice(NAUGHTY_STRINGS)
    return "".join(random.choices(string.ascii_letters, k=random.randint(1, 8)))

def rand_list():
    return [random.choice([rand_number(), rand_string()]) for _ in range(random.randint(0, 5))]



def simpleFuzzer(iterations_per_target: int = 30):
    errors = []
    for target in TARGETS:
        name = target.__name__
        for _ in range(iterations_per_target):
            try:
                if name == "safe_div":
                    a = random.choice([rand_number(), rand_string()])
                    b = random.choice([rand_number(), rand_string(), 0])
                    target(a, b)
                elif name == "to_int":
                    x = random.choice([rand_number(), rand_string()])
                    target(x)
                elif name == "concat_strings":
                    a = random.choice([rand_string(), rand_number()])
                    b = random.choice([rand_string(), rand_number()])
                    target(a, b)
                elif name == "list_index":
                    lst = rand_list()
                    idx = random.randint(-3, 5)
                    target(lst, idx)
                elif name == "sqrt_like":
                    x = random.choice([rand_number(), rand_string()])
                    target(x)
            except Exception as e:  # record the crash
                errors.append((name, repr(e)))

    # print at least 10 errors
    print("=== FUZZ SUMMARY ===")
    for i, (name, err) in enumerate(errors[:10], start=1):
        print(f"ERROR #{i}: {name} -> {err}")

    if not errors:
        print("No errors discovered.")


if __name__ == "__main__":
    simpleFuzzer()

