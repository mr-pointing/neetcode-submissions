class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out_num = 1
        stack_nums = []
        i = 0
        for i in tokens:
            if i == "+":
                stack_nums.append(stack_nums.pop() + stack_nums.pop())
            elif i == "-":
                x, y = stack_nums.pop(), stack_nums.pop()
                stack_nums.append(y - x)
            elif i == "*":
                stack_nums.append(stack_nums.pop() * stack_nums.pop())
            elif i == "/":
                x, y = stack_nums.pop(), stack_nums.pop()
                stack_nums.append(int( float(y)/ x))
            else:
                stack_nums.append(int(i))
        return stack_nums[0]
