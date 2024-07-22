class Solution:
    def makeGood(self, s: str) -> str:
        #we want to make our string good
        #two adjacent must not be the capital of the other
        #we can pop thatletter off the stack if the next is the upper or lowercase of it
        #then keep adding to the stack and return the final stack
        #edge cases
        #we also want to check if the stack is empty before we pop anything off
        
        
        #initialize stack and hash map
        stack = []
        hashMap ={"a":"A",
                 "b":"B",
                 "c":"C",
                 "d":"D",
                 "e":"E",
                 "f":"F",
                 "g": "G",
                 "h":"H",
                  "i":"I",
                  "j":"J",
                  "k":"K",
                  "l":"L",
                  "m":"M",
                  "n":"N",
                  "o":"O",
                  "p":"P",
                  "q":"Q",
                  "r":"R",
                  "s":"S",
                  "t":"T",
                  "u":"U",
                  "v":"V",
                  "w":"W",
                  "x":"X",
                  "y":"Y",
                  "z":"Z"}
        
        for letter in s:
            if not stack:
                stack.append(letter)
            else:
                if letter in hashMap:
                    if hashMap[letter] == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(letter)  
                else:
                    if stack[-1] in hashMap and hashMap[stack[-1]] == letter:
                        stack.pop()
                    else:
                        stack.append(letter)

        return "".join(stack)