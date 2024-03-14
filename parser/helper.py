from tokenizer import constants as constTokens
from . import constants as constParser

def searchString(tokens, start):
    string = []
    find_end = False
    end = 0
    for i in range(start + 1, len(tokens)):
        if tokens[i]['type'] == constTokens.symboleQuotationMark:
            find_end = True
            end = i
            break
        else:
            string.append(tokens[i]['value'])
    if not find_end:
        raise Exception(constParser.errorMissingQuotationMark)
    return {'type': constParser.typeString, 'value': ' '.join(string), 'start': start, 'end': end}

def search_args(tokens, start):
    if tokens[start]['type'] != constTokens.symboleOpenParenthese:
        raise Exception('Parenthèse ouvrante manquante.')
    find_end = False
    end = None
    args = []
    for i in range(start + 1, len(tokens)):
        if tokens[i]['type'] == constTokens.symboleCloseParenthese:
            find_end = True
            end = i
            break
        elif tokens[i]['type'] == constTokens.typeWord:
            args.append({'type': constParser.typeVariable, 'variableName': tokens[i]['value']})
        elif tokens[i]['type'] == constTokens.typeNumber['typeNumber']:
            args.append(tokens[i])
        elif tokens[i]['type'] == constTokens.symboleQuotationMark:
            temp = searchString(tokens, i)
            args.append(temp)
            i = temp['end']
    if not find_end:
        raise Exception('Parenthèse fermante manquante.')
    return {'args': args, 'end': end}