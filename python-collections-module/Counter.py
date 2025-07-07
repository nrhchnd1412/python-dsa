'''
Given a list of words Words = ["baby", "cat", "dada", "dog"] and a random jumbled string like ctay, write a function find(words, word1) that returns the word if it can be formed from the characters of the given string.
 - Example: 
 - find(words, "ctay") → returns "cat"
 - find(words, "dad") → returns "-" (not found)

Time: O(m + n * k)

O(m) for building frequency map of word1
O(n * k) for checking each word against the map

Space Complexity:
O(1) auxiliary (since alphabet size is fixed: 26 lowercase letters)
O(m) for Counter(word1)
'''
from collections import Counter


class FindWord:
    def create_freq(self,word):
        freq=[0]*26
        for ch in word:
            idx=ord(ch)-ord('a')
            freq[idx]+=1
        return freq
    
    def check_word(self,word,w):
        f1=self.create_freq(word)
        f2=self.create_freq(w)
        return bool(all(f1[idx]<=f2[idx] for idx in range(26)))

def find(words,w):
    w1=Counter(w)
    for word in words:
        w2=Counter(word)
        if w2<=w1:
            return word
    return "-"

words = ["baby", "cat", "dada", "dog"]
print(find(words, "ctay"))  # Output: "cat"
print(find(words, "dad"))   # Output: "-"
print(find(words, "god"))   # Output: "dog"
print(find(words, "abby"))  # Output: "baby"

f=FindWord()
print(f.check_word("cat","ctay")) # True
print(f.check_word("cats","ctay")) # False