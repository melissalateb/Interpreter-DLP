from tokenizer import constants as constTokens
from . import constants as constParser
from . import helper

def create(type, tokens, start):
    if type == constParser.expressionMethodCall:
        return objectMethodCall(tokens, start)
    elif type == constParser.expressionDeclaration:
        return variableDeclaration(tokens, start)
    elif type == constParser.expressionAffectation:
        return variableAffectation(tokens, start)

def objectMethodCall(tokens, start):
    objectName = tokens[start]['value']
    if tokens[start + 2]['type'] != constTokens.typeWord:
        raise ValueError(constParser.errorMissingWord)
    methodName = tokens[start + 2]['value']
    arguments = helper.search_args(tokens, start + 3)
    return {
        'type': constParser.expressionMethodCall,
        'objectName': objectName,
        'methodName': methodName,
        'arguments': arguments['args'],
        'end': arguments['end']
    }

def variableDeclaration(tokens, start):
    if tokens[start + 1]['type'] != constTokens.typeWord:
        raise ValueError(constParser.errorMissingWord)
    variableName = tokens[start + 1]['value']
    return {'type': constParser.expressionDeclaration, 'variableName': variableName}

def variableAffectation(tokens, start):
    if tokens[start - 1]['type'] != constTokens.typeWord:
        raise ValueError(constParser.errorMissingWord)
    variableName = tokens[start - 1]['value']
    variableValue = None
    if tokens[start + 1]['type'] == constTokens.typeNumber:
        variableValue = tokens[start + 1]
    elif tokens[start + 1]['type'] == constTokens.symboleQuotationMark:
        variableValue = helper.searchString(tokens, start + 1)
    return {'type': constParser.expressionAffectation, 'variableName': variableName, 'variableValue': variableValue}
