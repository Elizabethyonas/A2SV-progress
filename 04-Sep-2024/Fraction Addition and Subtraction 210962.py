# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        smplify_expression = "+".join(expression.split('/')).split("+")
        smplify_expression_list = []

        for i in range(len(smplify_expression)):
            if "-" in smplify_expression[i]:
                a,b = smplify_expression[i].split("-")
                if a != '': smplify_expression_list.append(a)
                smplify_expression_list.append("-"+b)
            else:
                smplify_expression_list.append(smplify_expression[i])

        lc = 1
        for i in range(len(smplify_expression_list)//2):
            lc = math.lcm(lc,int(smplify_expression_list[2*i+1]))

        total = 0
        for i in range(len(smplify_expression_list)//2):
            total += int(smplify_expression_list[2*i])*(lc//int(smplify_expression_list[2*i+1]))

        if total==0: 
            return "0/1"
        else: 
            return f"{total//math.gcd(total,lc)}/{lc//math.gcd(total,lc)}"