from egz3btesty import runtests

def uncool(P):
    indexed = [(a, b, i) for i, (a, b) in enumerate(P)]
    
    # sortujemy po początku rosnąco, a jeśli takie same — po końcu malejąco
    indexed.sort(key=lambda x: (x[0], -x[1]))

    max_end = -float('inf')
    max_idx = -1

    for a, b, idx in indexed:
        if a <= max_end and not (a >= indexed[max_idx][0] and b <= indexed[max_idx][1]):
            # mamy przecięcie i brak zawierania → niefajna para
            return (idx, indexed[max_idx][2])
        if b > max_end:
            max_end = b
            max_idx = indexed.index((a, b, idx))

    return None

# Uruchomienie testów
runtests(uncool, all_tests=True)
