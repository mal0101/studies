def process_data(liste, *args, precision = 2, prefix = "", suffix = ""):
    l1 = liste
    for arg in args:
        l1 = map(args, l1)
    l1 = filter(lambda x: x >= 0, l1)
    l1 = [f"{prefix}{round(precision)}{suffix}" for x in l1]
