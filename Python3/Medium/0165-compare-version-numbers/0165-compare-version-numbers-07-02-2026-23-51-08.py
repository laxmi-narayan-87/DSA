class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def string_length(s):
            count = 0
            while True:
                try:
                    _ = s[count]
                    count += 1
                except IndexError:
                    break
            return count

        n1, n2 = string_length(version1), string_length(version2)
        i = j = 0

        while i < n1 or j < n2:
            num1 = 0
            num2 = 0
            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + ("0123456789".find(version1[i]))
                i += 1
            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + ("0123456789".find(version2[j]))
                j += 1
            if num1 > num2: return 1
            if num1 < num2: return -1
            i += (i < n1)
            j += (j < n2)

        return 0
