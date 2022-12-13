import sys
 
def minimum_palindrome_count(string_len: int, in_string: str) -> int:

    memoization = [[False for column in range(0, string_len)] for row in range(string_len)]

    # seed table diagonally; all single letter substrings are palindromes
    for start_index in range(0, string_len):
        memoization[start_index][start_index] = True

    # O(n)
    # [2, 3, 4, 5]
    for substring_length in range(2, string_len + 1):
        # O(n^2)
        # [0, 1, 2, 3]
        for start_index in range(0, string_len - substring_length + 1):
            #in "aeroplane"
            # this would all result in
            # "ae", "er", "ro", "op", "pl" ...
            # "aer", "ero", "rop" ...
            # "aero", "erop", "ropl", ...
            # "aerop", "eropl", ...
            # "aeorpl"
            
            # A string is a palindrome if:
            # 1. The edges are a palindrome
            # 2. If inside of the string is a palindrome, excluding the edges.

            end_index = start_index + substring_length - 1
            do_edges_match = in_string[start_index] == in_string[end_index]
            if substring_length == 2:
                memoization[start_index][end_index] = do_edges_match
            else:
                is_palindrome_inside = memoization[start_index + 1][end_index - 1]
                memoization[start_index][end_index] = do_edges_match and is_palindrome_inside

    # Dynamic Programming Step 2 
    # cuts_needed[i] stores the minimum cuts for substring [0:i]
    cuts_needed = [0 for _ in range(0, string_len)]

    # O(n)
    for i in range(string_len):
        # We can't make any cuts, as the string itself is a palindrome so far.
        current_minimum_cuts = sys.maxsize
        if memoization[0][i] == True:
            # in bubbaseesabanana
            # it should be "bubba" "sees" "a" "banana"
            # So we split "bubba" out so far
            cuts_needed[i] = 1
        else:
            # O(n^2)
            # Once our current word say "aeeaoplane" reaches
            # "aeeao" then just start splitting it up, because it's no longer a palindrome.
            for j in range(0, i):
                # If the string with throwing away the left character is a palindrome,
                # and it needs less cuts than the previous palindrome - throw it away.
                if(memoization[j + 1][i] == True and current_minimum_cuts > cuts_needed[j] + 1):
                    current_minimum_cuts = cuts_needed[j] + 1
            
            cuts_needed[i] = current_minimum_cuts

    return cuts_needed[string_len - 1]


if __name__ == "__main__":
    string_length = input()
    string = input()
    print(minimum_palindrome_count(len(string), string))