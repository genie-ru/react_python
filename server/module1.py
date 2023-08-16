def find_max_position(n, s):
    pos = [*map(s.find, "A B C".split())]
    return max(pos) + 1