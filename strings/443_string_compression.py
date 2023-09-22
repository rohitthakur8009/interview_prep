"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
from typing import List

def compress(chars: List[str]) -> int:
    char_idx, write_idx = 0,0

    while char_idx < len(chars):
        curr = chars[char_idx]
        curr_count = 0
        while char_idx < len(chars) and chars[char_idx] == curr:
            curr_count += 1
            char_idx += 1
        if curr_count == 1:
            chars[write_idx] = curr
            write_idx += 1
        else:
            chars[write_idx] = curr
            write_idx += 1
            curr_count_string = str(curr_count)
            for c in curr_count_string:
                chars[write_idx] = c
                write_idx += 1

    return write_idx


test_cases = {
    "test1": {
        "input": {
            "chars": ["a","b","b","b","b","b","b","b","b","b","b","b","b"],
        },
        "result": 4
    },
    "test2": {
        "input": {
            "chars": ["a","a","b","b","c","c","c"]
        },
        "result": 6
    },
}

for test_case, test_data in test_cases.items():
    actual = compress(**test_data["input"])
    expected = test_data["result"]
    assert actual == expected, f"{test_case} : actual: {actual} is not equal to {expected}"