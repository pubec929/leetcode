
def find_index(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1

def find_index_v1(haystack: str, needle: str) -> int:
    comp_needle = list(needle)
    window = list(haystack[:len(needle)])

    if window == comp_needle:
        return 0
    for end_idx in range(len(needle), len(haystack)):
        window.pop(0)
        window.append(haystack[end_idx])
        if window == comp_needle:
            return end_idx - len(window) + 1
    return -1

if __name__ == "__main__":
    print(find_index_v1("hello", "ll"))