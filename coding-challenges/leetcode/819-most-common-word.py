"""
@author: acfromspace
"""

"""
Notes:

Find the most common word from a paragraph that can't be a banned word.
"""

from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        unbanned = []

        for character in "!?',;.":
            paragraph = paragraph.replace(character, " ")

        paragraph_list = paragraph.lower().split()

        for word in paragraph_list:
            if word not in banned:
                unbanned.append(word)

        # Get the `most_common` element, which holds a key value, which then we need the key.
        return Counter(unbanned).most_common(1)[0][0]


"""
Time complexity : O(p+b). "p" is the size of the `paragraph` and "b" is the size of `banned`.

Space complexity : O(p+b). To store the `paragraph_list` and the `banned` data structures.
"""
