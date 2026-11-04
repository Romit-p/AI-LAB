def pl_true(sentence, model):
    return sentence(model)


def tt_entails(kb, alpha, symbols):
    return tt_check_all(kb, alpha, symbols, {})


def tt_check_all(kb, alpha, symbols, model):

    if len(symbols) == 0:
        if pl_true(kb, model):
            return pl_true(alpha, model)
        else:
            return True

    p = symbols[0]
    rest = symbols[1:]

    model_true = model.copy()
    model_true[p] = True

    model_false = model.copy()
    model_false[p] = False

    return (tt_check_all(kb, alpha, rest, model_true)
            and
            tt_check_all(kb, alpha, rest, model_false))


def kb(model):
    P, Q, R = model['P'], model['Q'], model['R']

    return ((not Q or P)
            and (not P or not Q)
            and (Q or R))


def alpha(model):
    return model['R']


symbols = ['P', 'Q', 'R']

if tt_entails(kb, alpha, symbols):
    print("KB entails R")
else:
    print("KB does not entail R")
