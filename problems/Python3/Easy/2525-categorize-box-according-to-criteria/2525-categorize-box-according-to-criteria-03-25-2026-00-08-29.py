class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume=length*width*height
        if (length>=10**4 or width>=10**4 or height>=10**4 or volume>=10**9) and mass>=100:
            return "Both"
        elif length>=10**4 or width>=10**4 or height>=10**4 or volume>=10**9:
            return "Bulky"
        elif mass>=100:
            return "Heavy"
        else:
            return "Neither"