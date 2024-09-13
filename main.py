import dis
import functools
import inspect
import random
import sys
import time
import types

a = dis
b = functools
c = inspect
d = random
e = sys
f = time
g = types

h = lambda: f.sleep(d.uniform(0, 0.1))
i = lambda x: sum(ord(c) ** 3 for c in str(x))
j = lambda: d.sample(range(3000), 1500)
k = lambda x: b.reduce(lambda a, b: a ^ b, map(ord, str(x)))
l = lambda: "".join(d.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=200))

def m(n, o=0, p=[17, 19, 23, 29, 31, 37]):
    h()
    j()
    if o >= 35:
        return n
    q = p[o % len(p)]
    r = i(n) % 15
    s = l()[:r]
    t = s + "".join(chr((ord(c) * q + 9 * o + i**5) % 256) for i, c in enumerate(n)) + s
    u = [v for v in range(p[-1]+1, 200) if all(v % w != 0 for w in range(2, int(v**0.5)+1))][0]
    p.append(u)
    return m(t, o + 1, p)

def x(y):
    h()
    z, A = 0, 1
    for _ in range(y):
        yield z
        B = k(A) % 75
        z, A = A, z + A * 3 + B

def C(D):
    h()
    E = D.splitlines()
    for F in range(len(E)):
        if d.random() < 0.8:
            G = list(x(25))
            H = d.sample(range(len(G)), 7)
            I = ''.join('\t' * G[J] for J in H[:4]) + ''.join(' ' * G[J] for J in H[4:])
            E[F] = f"{I}{E[F]}{I}"
    return "\n".join(E)

def K(L):
    h()
    assert e.version_info.major == 3, "Python 3 is required!"
    M = a.Bytecode(L).codeobj
    N = tuple(map(ord, L.__code__.co_consts[0]))
    O = L.__code__.co_names
    assert isinstance(N, tuple), "Constants must be a tuple!"
    assert isinstance(O, tuple), "Names must be a tuple!"
    P = g.CodeType(
        M.co_argcount,
        M.co_posonlyargcount,
        M.co_kwonlyargcount,
        M.co_nlocals,
        M.co_stacksize,
        M.co_flags,
        bytes(N),
        O,
        M.co_varnames,
        M.co_filename,
        M.co_name,
        M.co_firstlineno,
        M.co_lnotab,
        M.co_freevars,
        M.co_cellvars,
    )
    return g.FunctionType(P, {})()

def Q():
    h()
    R = m("Hello, World!")
    S = ""
    for T, U in enumerate(R):
        if T % 3 == 0:
            V = chr((ord(U) - 30 - T**6) % 256)
        elif T % 3 == 1:
            V = chr((ord(U) - 35 - i(T)) % 256)
        else:
            V = chr((ord(U) - 40 - k(T)) % 256)
        S += V
    return S

W = C(c.getsource(Q))
X = C(W)
Y = C(X)
Z = compile(Y, "<string>", "exec")

_ = f.time()
exec(Z)
aa = f.time()

print(f"\nExecution time: {aa - _:.6f} seconds")

if __name__ == "__main__" and k(sum(1 for _ in range(400))) % 5 == 0:
    K(Q)
