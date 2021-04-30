def intersect(A, B):
    # linter = []
    # for cle in (dict(A).keys() & dict(B).keys()):
    #     linter.append(dict(A)[cle])
    #     linter.append(dict(B)[cle])
    # return set(linter)
    return {s[1] for s in A.union(B) if s[0] in (dict(A).keys() & dict(B).keys())}

print(intersect(
  { (1, 'unA'),
    (2, 'deux'),
    (3, 'troisA')},
  { (1, 'unB'),
    (2, 'deux'),
    (4, 'quatreB')}))