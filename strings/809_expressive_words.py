"""
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.



Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3


Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
"""

from typing import List


def expressiveWords(s: str, words: List[str]) -> int:
    res = 0

    for word in words:
        if s[-1] != word[-1]:
            continue
        sptr = 0
        wptr = 0
        word = list(word)
        expressed = True
        while wptr < len(word):
            curr = word[wptr]
            wctr = sctr = 0

            while wptr < len(word) and word[wptr] == curr:
                wptr = wptr + 1
                wctr = wctr + 1

            while sptr < len(s) and s[sptr] == curr:
                sptr = sptr + 1
                sctr = sctr + 1

            if sctr < wctr:
                expressed = False
                break

            if wctr == 1 and sctr != wctr and sctr <= wctr + 1:
                expressed = False
                break
            # wptr = wptr + 1
            # sptr = sptr + 1
            print(wptr, sptr, wctr, sctr)
        if expressed and sptr >= len(s) - 1:
            res = res + 1

    return res


test_cases = {
    "test1": {
        "input": {
            "s": "heeellooo",
            "words": ["hello", "hi", "helo"],
        },
        "result": 1
    },
    "test2": {
        "input": {
            "s": "zzzzzyyyyy",
            "words": ["zzyy", "zy", "zyy", "zzzzzyyyyy"],
        },
        "result": 4
    },
    "test3": {
        "input": {
            "s": "abcd",
            "words": ["abc"],
        },
        "result": 0
    }

}


for test_case, test_data in test_cases.items():
    actual = expressiveWords(**test_data["input"])
    expected = test_data["result"]
    assert actual == expected, f"{test_case} : actual: {actual} is not equal to {expected}"
