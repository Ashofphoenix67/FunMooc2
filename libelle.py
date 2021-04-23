def libelle(ligne):
    try:
        prenom, nom, etage = ligne.split(sep=",")
        if etage == ' ':
            mes = '-ème'
        else:
            mes = etage.strip() + ("er" if int(etage) <= 1 else "-ème")

        return (f"{nom.strip()}.{prenom.strip()} ({mes})")
    except ValueError:
        return None

print(libelle('\t John, Doe\t, '))