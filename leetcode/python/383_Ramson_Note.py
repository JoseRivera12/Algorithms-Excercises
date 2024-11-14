class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapping = Counter(magazine)
        
        for letter in ransomNote:
            if letter not in mapping:
                return False
            if mapping[letter] < 1:
                return False
            mapping[letter] -= 1
        
        return True
