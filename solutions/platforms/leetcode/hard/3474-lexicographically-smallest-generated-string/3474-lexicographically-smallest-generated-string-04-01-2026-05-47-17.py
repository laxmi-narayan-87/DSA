class Solution:
    def generateString(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        sz = n + m - 1
        word = ['$'] * sz
        for i in range(n):
            if s1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '$':
                        word[i + j] = s2[j]
                    elif word[i + j] != s2[j]:
                        return ""
        for i in range(n):
            if s1[i] == 'F':
                cntBlank = 0
                cntSame = 0
                lastBlank = -1
                for j in range(m):
                    if word[i + j] == '$':
                        cntBlank += 1
                        lastBlank = i + j
                    if word[i + j] == s2[j]:
                        cntSame += 1
                if cntSame == m and cntBlank == 0:
                    return ""
                if cntSame == m and cntBlank > 0:
                    idx = lastBlank
                    j = idx - i  
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != s2[j]:
                            word[idx] = c
                            break
        for i in range(sz):
            if word[i] == '$':
                word[i] = 'a'
        return ''.join(word)