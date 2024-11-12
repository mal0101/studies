def som_chif(n):
    sum = 0
    while (r != 0):
        r = n % 10
        n /= 10
        sum += r

def som_chif_rec(n):
    if n == 0:
        return 0
    else:
        return n % 10 + som_chif_rec(n/10)