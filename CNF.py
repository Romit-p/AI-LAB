
print("Enter an English FOL statement:")
sentence = input().lower().strip()

if sentence == "everyone who loves all animals is loved by someone":

    print("\nStep 1: English to FOL")

    print("ForAll x [(ForAll y [Animal(y) -> Loves(x,y)]) -> Exists z Loves(z,x)]")

    print("\nStep 2: Eliminate biconditional")
    print("No biconditional present")

    print("\nStep 3: Eliminate implication")

    print("ForAll x [NOT ForAll y [NOT Animal(y) OR Loves(x,y)] OR Exists z Loves(z,x)]")

    print("\nStep 4: Move negations inward")

    print("ForAll x [Exists y [Animal(y) AND NOT Loves(x,y)] OR Exists z Loves(z,x)]")

    print("\nStep 5: Standardize variables")
    print("ForAll x [Exists y [Animal(y) AND NOT Loves(x,y)] OR Exists z Loves(z,x)]")

    print("\nStep 6: Skolemization")
    print("ForAll x [(Animal(f(x)) AND NOT Loves(x,f(x))) OR Loves(g(x),x)]")

    print("\nStep 7: Drop universal quantifiers")
    print("(Animal(f(x)) AND NOT Loves(x,f(x))) OR Loves(g(x),x)")

    print("\nStep 8: Distribute OR over AND")

    print("(Animal(f(x)) OR Loves(g(x),x))")
    print("AND")
    print("(NOT Loves(x,f(x)) OR Loves(g(x),x))")

    print("\nStep 9: Final CNF")
    print("(Animal(f(x)) OR Loves(g(x),x))")
    print("AND")
    print("(NOT Loves(x,f(x)) OR Loves(g(x),x))")

else:
    print("Sentence pattern not supported.")
