import this

def decode_zen(this_module):
    """
    dÃ©code le zen de python Ã  partir du module this
    """
    # la version encodÃ©e du manifeste
    encoded = this_module.s
    # le dictionnaire qui implÃ©mente le code
    code = this_module.d
    # si un caractÃ¨re est dans le code, on applique le code
    # sinon on garde le caractÃ¨re tel quel
    # aussi, on appelle 'join' pour refaire une chaÃ®ne Ã  partir
    # de la liste des caractÃ¨res dÃ©codÃ©s
    return ''.join(code[c] if c in code else c for c in encoded)

decode_zen(this)
