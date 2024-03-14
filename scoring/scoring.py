from tokenizer.tokenizer import Tokenizer
from parser.parser import parse
from .helper import allDeclaredIsUsed, allUsedIsDeclared, allExpressionFinished, numberLine, indentation, calculate_score
import json
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.web import JsonLexer

def analyze(code):
    print("-------- Tokens --------")
    tokens = Tokenizer.tokenize(code)
    pretty_json = json.dumps(tokens, indent=4)
    colorful = highlight(
    pretty_json,
    lexer=JsonLexer(),
    formatter=Terminal256Formatter())

    print(colorful)



    try:
        print("-------- AST --------")
        ast = parse(tokens)
        jsonAST = json.dumps(ast, indent=4)
        colorful = highlight(
            jsonAST,
            lexer=JsonLexer(),
            formatter=Terminal256Formatter())
        print(colorful)
        result = {
            'allDeclaredIsUsed': allDeclaredIsUsed(ast),
            'allUsedIsDeclared': allUsedIsDeclared(ast),
            'allExpressionFinished': allExpressionFinished(ast),
            'numberLine': numberLine(ast),
            'indentation': indentation(ast)
        }
        return {
            'score': calculate_score(ast),
            'details': result
        }
    except Exception as e:
        raise e
