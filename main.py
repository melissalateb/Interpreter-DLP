from scoring import scoring
import json
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.web import JsonLexer

def main():
    try:
        with open("test.js", "r", encoding="utf8") as file:
            code = file.read()

        score = scoring.analyze(code)
        print("--------", "Result", "--------")
        pretty_json = json.dumps(score, indent=4)
        colorful = highlight(
            pretty_json,
            lexer=JsonLexer(),
            formatter=Terminal256Formatter())
        print(colorful)
    except FileNotFoundError:
        print("Error: File 'test.js' not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
