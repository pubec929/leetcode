"""https://leetcode.com/problems/unique-morse-code-words/description/"""
MORSE_CODE_DICT = {
    'a': '.-',     'b': '-...',   'c': '-.-.',   'd': '-..',    'e': '.',
    'f': '..-.',   'g': '--.',    'h': '....',   'i': '..',     'j': '.---',
    'k': '-.-',    'l': '.-..',   'm': '--',     'n': '-.',     'o': '---',
    'p': '.--.',   'q': '--.-',   'r': '.-.',    's': '...',    't': '-',
    'u': '..-',    'v': '...-',   'w': '.--',    'x': '-..-',   'y': '-.--',
    'z': '--..'
}

def translate(word: str) -> str:
    code = ""
    for letter in word:
        code += MORSE_CODE_DICT[letter]
    return code

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        unique = set()
        for w in words:
            unique.add(translate(w))
        return len(unique)

