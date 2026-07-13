class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#Hello5#World1#!
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        result = []
        while i < len(s):
            word_length = ""
            while s[j] != "#":
                word_length += s[j]
                j += 1
            word_start, word_end = j+1, j+1+int(word_length)
            result.append(s[word_start:word_end])
            i = j = word_end

        return result