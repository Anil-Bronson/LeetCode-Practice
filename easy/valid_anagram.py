# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.

def isAnagram(s: str, t: str) -> bool:
    if set(s) == set(t):
        return True
    return False


s = "rat"
t = "car"

print(isAnagram(s,t))