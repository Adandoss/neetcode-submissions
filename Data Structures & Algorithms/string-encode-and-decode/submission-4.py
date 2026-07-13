class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#Hello5#World1#!
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            word_length = ""
            while s[i] != "#":
                word_length += s[i]
                i += 1
            word_start, word_end = i+1, i+1+int(word_length)
            result.append(s[word_start:word_end])
            i = word_end

        return result