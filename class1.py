class Phrase:
    def __init__(self, phrase):
        self.mots = phrase.split()

    def upper(self):
        self.mots = [m.upper() for m in self.mots]

    def __str__(self):
        return '\n'.join(self.mots)

p = Phrase('je fais un mooc sur python')

print(p.mots)
p.upper()
print(p.mots)
print(p)

