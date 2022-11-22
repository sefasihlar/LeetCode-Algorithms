class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        lookup = {")":"(","}":"{","]":"["}
        print(lookup)
        
        for i in s:
            if i in lookup.values():
                print(i)
                stack.append(i)
            elif stack and lookup[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack  == []