class Exp:
    def __init__(self, input):
        self.input = input
        self.infix = []
        self.postfix = []
        self.str_to_infix()
        self.infix_to_postfix()
        print(self.postfix)

    def str_to_infix(self):
        temp = ""
        for c in self.input:
            if c.isdecimal() or c == '.':
                temp += c
            elif c in '()^/*+-':
                if temp != '':
                    self.infix.append(float(temp))
                self.infix.append(c)
                temp = ""
            else:
                print("invalid")
                exit(1)
        self.infix.append(float(temp))

    def infix_to_postfix(self):
        precedence = {'^': -1, '/': -2, '*': -3, '+': -4, '-': -5}
        stack = []
        for x in self.infix:
            if isinstance(x, float):
                self.postfix.append(x)
            elif x in precedence:
                if len(stack) == 0 or precedence[x] > precedence[stack[-1]] or '(' in stack:
                    stack.append(x)
                else:
                    while precedence[x] <= precedence[stack[-1]] or stack[-1] != '(':
                        self.postfix.append(stack.pop())
                        stack.append(x)
            elif x=='(':
                stack.append(x)
            elif x==')':
                while stack[-1] != '(':
                    self.postfix.append(stack.pop())
                stack.pop()


if __name__ == "__main__":
    while True:
        Exp("(1+0.1)/0.01*100")
