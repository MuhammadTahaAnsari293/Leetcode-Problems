class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle_string = [0] * len(s)
        j=0
        for i in indices:
            shuffle_string[i]=s[j]
            j+=1
        return "".join(shuffle_string)
        