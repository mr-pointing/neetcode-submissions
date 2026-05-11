class Solution:
    def isValid(self, s: str) -> bool:
        open_dict = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        current = []
        for i in s:
            if i in open_dict.keys():
                current.append(open_dict[i])
            elif len(current) >= 1 and i == current[-1]:
                current.pop()
            else:
                return False
        return True if not current else False
        

                

        