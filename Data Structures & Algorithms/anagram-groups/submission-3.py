class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            word_tuple = self.create_word_tuple(s)
            anagrams_dict[word_tuple].append(s)

        return list(anagrams_dict.values())

    def create_word_tuple(self, word:str) -> tuple[int, ...]:
        word_array = [0] * 26
        for c in word:
            letter = ord(c) - 97
            word_array[letter] += 1
        return tuple(word_array)