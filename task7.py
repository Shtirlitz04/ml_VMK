def find_modified_max_argmax(L, f):
    N = [f(i) for i in L if type(i)==int]
    if N:
        return (m:=max(N), N.index(m))
    else:
        return()
