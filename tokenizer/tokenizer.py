from . import helper
from . import constants as constTokens
import re

class Tokenizer:
    def tokenize(code):
        code = helper.replaceSpecialsChars(code)

        # Préparation des expressions régulières pour capturer aussi les espaces et les sauts de ligne
        token_specification = [
            ('NEWLINE', r'\n'),                     # Sauts de ligne
            ('SPACE', r'[ \t]+'),                   # Espaces et tabulations
            ('NUMBER', r'\d+(\.\d*)?'),             # Nombres
            ('WORD', r'[A-Za-z]+'),                 # Mots
            # Ajouter ici des règles pour d'autres types de tokens
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

        tokens = []
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            if kind in ('NEWLINE', 'SPACE'):
                # Traitement spécifique pour newLine et space si nécessaire
                continue  # Exemple : ignorer les espaces et les sauts de ligne si non nécessaires
            if kind == 'NUMBER':
                tokens.append({'type': constTokens.typeNumber, 'value': value})
            elif kind == 'WORD':
                # Vérifier si le mot correspond à un caractère spécial
                type_chars = helper.checkChars(value)
                if type_chars:
                    tokens.append({'type': type_chars, 'value': value})
                else:
                    tokens.append({'type': constTokens.typeWord, 'value': value})
            # Ajouter des conditions pour d'autres types de tokens ici

        if len(tokens) < 1:
            raise Exception(constTokens.errorNoTokenFound)
        return tokens
