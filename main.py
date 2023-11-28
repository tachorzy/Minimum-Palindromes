import math
import functools

def minimum_palindrome(length: int, string: str) -> int:
    if length == 0:
        return 0
    table =  [[False for col in range(length)] for row in range(length)]
    cuts = list(range(length + 1))

    for start in range(1, length):
        mincut = math.inf
        for end in range(start + 1):
            do_edges_match = string[start] == string[end]
            is_start_inbounds = start <= end + 1
            if do_edges_match and (is_start_inbounds or table[start - 1][end + 1]):
                table[start][end] = True
                mincut = min(mincut, 1 + cuts[end - 1])
        cuts[start] = mincut

    return cuts[length - 1] + 1

def min_palindrome_rec(string: str) -> int:
    @functools.cache
    def is_palindrome(i, j):
        if i >= j:
            return True
        else:
            return string[i] == string[j] and is_palindrome(i + 1, j - 1)
    @functools.cache
    def min_cut(i):
        # returns minimum palindrome whatever on substring 0...i - 1
        if i <= 0:
            return True
        else:
            return min(min_cut(j) + 1 for j in range(i) if is_palindrome(j, i))
    return min_cut(len(string))

if __name__ == "__main__":
    string_length = input()
    string = input()
    print(minimum_palindrome(len(string), string))
