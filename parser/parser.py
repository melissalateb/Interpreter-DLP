from tokenizer import constants as constTokens
from . import constants as constParser
from . import expressionsFactory as factory

def parse(tokens):
    AST = []
    i = 0
    current_indentation = 0  # Track the current level of indentation
    
    while i < len(tokens):
        expression = None
        # Detect and update indentation level at new lines
        if tokens[i]['type'] == constTokens.typeNewLine:
            i += 1  # Skip the newline token
            indentation_count = 0  # Reset indentation count for new line
            # Count the number of spaces to determine the new indentation level
            while i < len(tokens) and tokens[i]['type'] == constTokens.typeSpace:
                indentation_count += len(tokens[i]['value'])  # Assuming the 'value' holds the actual spaces
                i += 1
            current_indentation = indentation_count // 4  # Assuming 4 spaces per indentation level; adjust as needed

        if tokens[i]['type'] == constTokens.typeWord and tokens[i]['value'] in constParser.declarationVariable:
            expression = factory.create(constParser.expressionDeclaration, tokens, i)
            i += 1

        elif tokens[i]['type'] == constTokens.symboleEqual:
            expression = factory.create(constParser.expressionAffectation, tokens, i)

            if expression['variableValue']['type'] == constTokens.typeNumber:
                i += 1

            else:
                i = expression['variableValue']['end']
                
        elif i < len(tokens) - 1 and tokens[i]['type'] == constTokens.typeWord and tokens[i + 1] == constTokens.symbolePoint:
            expression = factory.create(constParser.expressionMethodCall, tokens, i)
            i = expression['end']
        if expression:
            AST.append(expression)
        else:
            AST.append(tokens[i])
        i += 1
    return AST
