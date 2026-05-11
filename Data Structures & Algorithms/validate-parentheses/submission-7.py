class Solution:
    def isValid(self, s: str) -> bool:
        openers = ['(', '[', '{']
        closers = [')', ']', '{']
        open_dict = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        current = []
        if len(s) > 1:
            for i in s:
                if i in open_dict.keys():
                    current.append(open_dict[i])
                elif len(current) >= 1 and i == current[-1]:
                    current.pop()
                else:
                    return False
            if len(current) == 0:
                return True
        return False

                

        