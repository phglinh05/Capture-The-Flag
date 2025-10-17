def extended_euclidean(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

    return r0, s0, t0

p = 26513
q = 32321
gcd, u, v = extended_euclidean(p, q)
print("u:", u)
print("v:", v)
