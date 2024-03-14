def allDeclaredIsUsed(ast):
    declared_variables = set()
    used_variables = set()
    
    # Parcours de l'AST pour collecter les déclarations et les utilisations
    for node in ast:
        if node['type'] == 'variableDeclaration':
            declared_variables.add(node['variableName'])
        elif node['type'] == 'variableAffectation':
            used_variables.add(node['variableName'])
        # elif node['type'] == 'expressionMethodCall':
        #     used_variables.add(node['objectName'])  # Ajouter le nom de l'objet
        #     for arg in node['arguments']:
        #         if arg['type'] == 'variable':
        #             used_variables.add(arg['value'])  # Ajouter les arguments de méthode

    # Calcul du score en fonction de la proportion de variables déclarées utilisées
    if not declared_variables:
        return 0  # Score 0 si aucune variable n'est déclarée
    score = min(10, max(0, 10 * len(used_variables.intersection(declared_variables)) / len(declared_variables)))
    return round(score, 2)


def allUsedIsDeclared(ast):
    declared_variables = set()
    used_variables = set()

    for node in ast:
        if node['type'] == 'variableDeclaration':
            declared_variables.add(node['variableName'])
        elif node['type'] == 'variableAffectation':
            # Vérifiez que la variable affectée a été déclarée
            used_variables.add(node['variableName'])

    # Vérifiez que chaque variable utilisée a été déclarée
    undeclared_variables_usage = used_variables - declared_variables

    if undeclared_variables_usage:
        # Si il y a des variables utilisées non déclarées, ajustez le score en conséquence
        score = min(10, max(0, 10 * (1 - len(undeclared_variables_usage) / len(used_variables))))
    else:
        # Si toutes les variables utilisées ont été déclarées, le score est maximal
        score = 10

    return round(score, 2)

def allExpressionFinished(ast):
    special_chars = {
        'point': '.',
        # Ajoutez d'autres caractères spéciaux si nécessaire
    }
    symbole_virgule = ','

    score = 10  # Score par défaut
    strings = set()

    # Collecte de toutes les chaînes de caractères dans le code
    for node in ast:
        if node['type'] == 'variableAffectation' and node['variableValue']['type'] == 'string':
            strings.add(node['variableValue']['value'])

    # Vérification de chaque chaîne de caractères pour voir si elle constitue une phrase complète
    for string_value in strings:
        if string_value.endswith(special_chars['point']):
            # Vérifie si la chaîne de caractères se termine par un point
            if symbole_virgule in string_value:
                # Vérifie si la chaîne de caractères contient une virgule
                continue
            else:
                score -= 2  # Déduire 2 points si la phrase ne contient pas de virgule
        else:
            score -= 5  # Déduire 5 points si la phrase ne se termine pas par un point

    # Assurer que le score est compris entre 0 et 10
    score = max(0, min(10, score))
    return round(score, 2)






def indentation(ast):
    # Cette fonction est un exemple hypothétique, supposant que chaque noeud AST contienne une propriété 'indentation'
    correct_indentations = 0
    total_indentable_nodes = 0

    for node in ast:
        if node['type'] in ['variableDeclaration', 'variableAffectation']:
            total_indentable_nodes += 1
            # Hypothétiquement, si votre AST incluait une propriété 'indentation' pour chaque noeud:
            # Supposons qu'un niveau d'indentation correct soit de 4 espaces.
            # Cette vérification est simplifiée et hypothétique.
            if node.get('indentation', 0) % 4 == 0:
                correct_indentations += 1

    # Si aucun noeud n'a besoin d'indentation, considérez cela comme correct.
    if total_indentable_nodes == 0:
        return 10

    # Calculez le score basé sur la proportion de noeuds correctement indentés.
    score = (correct_indentations / total_indentable_nodes) * 10
    return round(score, 2)


def numberLine(ast):
    line_count = 1
    max_lines = 200
   
    for node in ast:
        if node['type'] == 'newLine':
            line_count += 1
   
    if line_count > max_lines:
        score_value = 0
    else:
        score_value = 10


    return score_value

def calculate_score(ast):
    all_declared_used_score = allDeclaredIsUsed(ast)
    all_used_declared_score = allUsedIsDeclared(ast)
    all_expression_finished_score = allExpressionFinished(ast)
    indentation_score = indentation(ast)  
    number_line_score = numberLine(ast)
    
    total_score = (all_declared_used_score + all_used_declared_score +
                   all_expression_finished_score + indentation_score + number_line_score)
    normalized_score = (total_score / 50) * 10 
    
    return round(normalized_score, 2)