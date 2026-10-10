class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        i=len(s)-1
        while i>=0 and s[i] in vowels:
            i-=1
        return s[:i+1]