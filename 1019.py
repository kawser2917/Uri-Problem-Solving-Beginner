N = int(input())
H = int(N/3600)
M = int((N%3600)/60)
S = int((N%3600)%60)
print(f"{H}:{M}:{S}")