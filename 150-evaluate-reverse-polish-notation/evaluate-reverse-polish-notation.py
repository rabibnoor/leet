def trunc_div(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


class Solution(object):
    def eval(self,op, v1, v2):
        if op == "+":
            return v1+v2
        if op == "-":
            return v1-v2
        if op == "*":
            return v1*v2
        if op == "/":
            return trunc_div(v1,v2)
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        myl = []
        for i in tokens:
            #print(myl)
            if i in ["+", "-", "*", "/"]:
                v2 = myl.pop()
                v1 = myl.pop()
                v3 = self.eval(i, v1, v2)
                myl.append(v3)
            else:
                myl.append(int(i))

        if myl:
            #print(myl)
            return myl[-1]

        