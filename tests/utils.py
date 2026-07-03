import uuid


def generate_random_color():
    import random
    return "{:06x}".format(random.randint(0, 0xFFFFFF))

def suid() -> str:
    return str(uuid.uuid4().hex[:8])