"""https://leetcode.com/problems/most-common-word/"""
from collections import Counter

def split_words(paragprah: str, banned: set[str]):
    symbols = set("!?',;. ")
    w = ""
    for char in paragprah.lower() + " ":
        if char in symbols and w != "":
            if w not in banned:
                yield w
            w = ""
        if char not in symbols:
            w += char

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        counter = Counter()
        for w in split_words(paragraph, set(banned)):
            counter[w] += 1
        return max(counter, key=counter.get)
