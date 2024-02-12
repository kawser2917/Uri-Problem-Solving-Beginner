t = int(input())
for i in range(t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    ct = 0
    while (pa <= pb):
        cpa = int((pa * (g1 / 100)))
        cpb = int((pb * (g2 / 100)))
        ct += 1
        pa += cpa
        pb += cpb
        if (ct > 100):
            break
    if (ct > 100):
        print("Mais de 1 seculo.")
    else:
        print(f"{ct} anos.")