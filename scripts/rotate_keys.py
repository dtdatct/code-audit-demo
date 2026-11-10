import random


def new_key():
    return "".join(random.choice("0123456789abcdef") for _ in range(32))


if __name__ == "__main__":
    key = new_key()
    print("new key:", key)
    with open("/tmp/keys.txt", "w") as fh:
        fh.write(key)
