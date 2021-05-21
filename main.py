class Exp:
    def __init__(self, input):
        self.input = input
        self.infix = []
        self.postfix = []
        self.str_to_infix()
        self.infix_to_postfix_indices()
        self.print_infix()
        self.evaluate_steps()

    def str_to_infix(self):
        temp = ""
        for c in self.input:
            if c in ', ':
                continue
            elif c.isdecimal() or c == '.':
                temp += c
            elif c in '()^/*+-':
                if temp != '':
                    self.infix.append(float(temp))
                self.infix.append(c)
                temp = ""
            else:
                print("invalid")
                exit(1)
        if temp!='':
            self.infix.append(float(temp))

    def infix_to_postfix_indices(self):
        precedence = {'^': -1, '/': -2, '*': -3, '+': -4, '-': -5}
        stack = []

        for i, x in enumerate(self.infix):
            if isinstance(x, float):
                self.postfix.append(i)
            elif x in precedence:
                if len(stack) == 0 or self.infix[stack[-1]] == '(' or precedence[x] > precedence[self.infix[stack[-1]]]:
                    stack.append(i)
                else:
                    while len(stack) > 0 and (precedence[x] <= precedence[self.infix[stack[-1]]] or self.infix[stack[-1]] != '('):
                        self.postfix.append(stack.pop())
                    stack.append(i)
            elif x == '(':
                stack.append(i)
            elif x == ')':
                while self.infix[stack[-1]] != '(':
                    self.postfix.append(stack.pop())
                stack.pop()

        while len(stack) > 0:
            self.postfix.append(stack.pop())

    def evaluate_steps(self):
        stack = []
        step_num = 0
        for x in self.postfix:
            if isinstance(self.infix[x], float):
                stack.append(x)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                operator = self.infix[x]
                exp = str(self.infix[operand1]) + \
                    operator+str(self.infix[operand2])
                result = eval(exp)
                self.infix[operand1] = ''
                self.infix[operand2] = ''
                self.infix[x] = result
                stack.append(x)
                step_num += 1
                self.add_step(step_num, operator, exp)

    def add_step(self, step_num, operator, exp):
        current_exp = ''
        operation = ''
        if operator == '^':
            operation = 'Rasing to the power'
        elif operator == '/':
            operation = 'Performing division'
        elif operator == '*':
            operation = 'Performing multiplication'
        elif operator == '+':
            operation = 'Performing addition'
        elif operator == '-':
            operation = 'Performing subtraction'

        for x in self.infix:
            current_exp += str(x)
            current_exp = current_exp.replace('()', '')

        print(
            f'Step {step_num}: {operation}, {exp}\n\t{current_exp}', end='\n\n')

    def print_postfix(self):
        for x in self.postfix:
            print(self.infix[x], end='')

    def print_infix(self):
        for x in self.infix:
            print(x, end=' ')
        print('\n\n')


if __name__ == "__main__":
    Exp(input("Enter expression: "))
