## Infinite odd number sequence
def odd_inf_seq():
    a = 1
    while True:
        yield a
        a += 2
seq = odd_inf_seq()
print(next(seq))
print(next(seq))
print(next(seq))
    
