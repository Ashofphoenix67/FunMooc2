class Fifo:
    def __init__(self):
        self.pile = []
    def incoming(self, value):
        self.pile.append(value)
    def outgoing(self):
        try:
            return self.pile.pop(0)
        except IndexError:
            None

F = Fifo()
F.outgoing()
F.incoming(1)
F.incoming(2)
print(F.outgoing())
print(F.outgoing())
print(F.outgoing())

