import random


def list_equal(ol, tl):
    if len(ol) != len(tl):
        return False
    ol, tl = sorted(ol), sorted(tl)
    for i in range(len(ol)):
        if ol[i] != tl[i]:
            return False
    return True


def inv_below(i, x):
    target_bit = i.bit_length()
    target_bit %= 32
    target_bit = 32 - target_bit
    return x << target_bit


def inv_shuffle(ol, tl):
    if len(ol) >= 2 ** 32:
        raise Exception('you cannot enter an array longer than 32 bits')
    if not list_equal(ol, tl):
        raise Exception('origin_list and target_list do not match')

    rs = []
    for i in reversed(range(1, len(ol))):
        current_value = tl[i]
        original_index = ol.index(current_value)
        rs.append(original_index)
        ol[i], ol[original_index] = ol[original_index], ol[i]

    res = []
    k = 0
    for i in reversed(range(1, len(ol))):
        res += [inv_below(i + 1, rs[k])]
        k += 1
    return res


def test():
    from random_util import find_seed
    origin_list = [1, 2, 3, 7, 6, 4]
    target_list = [3, 2, 1, 4, 7, 6]
    print(f'the origin list is {origin_list}')
    print(f'the target list is {target_list}')
    rands = inv_shuffle(origin_list, target_list)
    seed_int = find_seed(rands)
    random.seed(seed_int)
    origin_list = [1, 2, 3, 7, 6, 4]
    random.shuffle(origin_list)
    print(f'after seed, the final list is {origin_list}')


if __name__ == '__main__':
    test()

