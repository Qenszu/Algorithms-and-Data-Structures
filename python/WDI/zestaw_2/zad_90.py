def check_mask(mask1, mask2, n):
    if mask1 | mask2 != 2**n - 1:
        return False
    return True


def generate_sums(tab1, tab2):
    size = len(tab1)
    for i in range(1, 2**size - 1):
        for j in range(1, 2**size - 1):
            if check_mask(i, j, size):
                x = 1