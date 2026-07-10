class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            word_tuple = self.create_word_tuple(s)
            anagrams_dict[word_tuple].append(s)

        final_list = []
        for annagrams in anagrams_dict.values():
            final_list.append(annagrams)
            
        return final_list

    def create_word_tuple(self, word:str) -> tuple[int, ...]:
        word_array = [0] * 26
        for c in word:
            letter = ord(c) - 97
            word_array[letter] += 1
        return tuple(word_array)