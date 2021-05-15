from visma.simplify.simplify import simplify
from visma.io.tokenize import tokenizer
from visma.io.parser import resultStringCLI

inputAgain = True
while(inputAgain):
    inputAgain = False
    inputExp = input('Enter mathematical expression: ')
    tokens, _, _, equationTokens, comments = simplify(tokenizer(inputExp))
    print(resultStringCLI(equationTokens, 'simplify', comments, 'expression', False))
    inputAgainStr = input('Calculate another expression? (y/n): ')
    if inputAgainStr == 'y':
        inputAgain = True
