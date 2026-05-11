class Solution:
    def isValid(self, s: str) -> bool:
        o_dict = {'(':')', '[':']', '{':'}'}
        current = [] 
        for v in s:
            if v in o_dict.keys():
                current.append(o_dict[v])
            elif len(current) >= 1 and v == current[-1]:
                current.pop()
            else:
                return False
        return True if not current else False 