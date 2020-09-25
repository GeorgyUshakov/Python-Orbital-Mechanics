import matplotlib.pyplot as plt

P1 = 18.868
P2 = 28.699

def eq(p,q):
    P = q/(((p+q)/P2)-(p/P1))
    return P

print(eq(1,3))
print(eq(1,2))
print(eq(2,3))
print(eq(1,1))
print(eq(3,2))
print(eq(2,1))
