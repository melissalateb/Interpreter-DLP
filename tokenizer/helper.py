from . import constants as constTokens
import re


def checkChars(t):
    for char_name, reg_rule in constTokens.specialChars.items():
        if t == f'*{char_name}*':
            return char_name
    return False

def replaceSpecialsChars(code):
    for char_name, element in constTokens.specialChars.items():
        code = re.sub(element['regRule'], f' *{char_name}* ', code)
    return code