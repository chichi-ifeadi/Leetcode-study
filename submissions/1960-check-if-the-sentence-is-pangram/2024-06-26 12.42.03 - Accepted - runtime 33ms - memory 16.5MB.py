class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #check if length of str 

        seen = set()
        for char in sentence:
            if char not in seen:
                seen.add(char)

        if len(seen)== 26:
            return True
        return False

            