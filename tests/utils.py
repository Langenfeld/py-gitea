def generate_random_color():
    import random
    return "{:06x}".format(random.randint(0, 0xFFFFFF))