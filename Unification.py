def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    if x == y:
        return subst

    if isinstance(x, str) and x.islower():
        if x in subst:
            return unify(subst[x], y, subst)
        if occurs(x, y, subst):
            return "FAILURE"
        subst[x] = y
        return subst

    if isinstance(y, str) and y.islower():
        return unify(y, x, subst)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return "FAILURE"

        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)
            if subst == "FAILURE":
                return "FAILURE"
        return subst

    return "FAILURE"


def occurs(var, x, subst):
    if var == x:
        return True
    if isinstance(x, tuple):
        return any(occurs(var, i, subst) for i in x)
    return False


p1 = ("Knows", "x", "John")
p2 = ("Knows", "Mary", "y")

result = unify(p1, p2)

if result == "FAILURE":
    print("Unification Failed!")
else:
    print("Unification Successful!")
    print("Substitution:", result)
