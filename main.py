import sys

def minimum_palindrome(length: int, string: str) -> int:
    if(length == 0):
        return 0
    table =  [[False for col in range(length)] for row in range(length)]
    cuts = [0 for _ in range(length)]

    for start in range(1,length):
        mincut = sys.maxsize
        for end in range(start+1):
            do_edges_match = string[start] == string[end]
            is_start_inbounds = start<=end+1
            if(do_edges_match and (is_start_inbounds or table[start-1][end+1])):
                table[start][end] = True
                mincut = min(mincut, 0 if end == 0 else 1 + cuts[end-1])
        cuts[start] = mincut

    return cuts[length-1]+1

if __name__ == "__main__":
    string_length = input()
    string = input()
    print(minimum_palindrome(len(string), string))