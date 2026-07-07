class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count_1 = defaultdict(int)
        letter_count_2 = defaultdict(int)
        for c in s:
            letter_count_1[c] += 1
        for c in t:
            letter_count_2[c] += 1
        
        if letter_count_1.keys() != letter_count_2.keys():
            return False

        for key in letter_count_1.keys():
            if letter_count_1[key] != letter_count_2[key]:
                return False

        return True

        