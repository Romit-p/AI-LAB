
import random

def cost(state):
    n = len(state)
    attacks = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                attacks += 1

    return attacks


def display(state):
    n = len(state)

    for row in range(n):
        for col in range(n):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def best_successor(state):
    n = len(state)
    best = state
    best_cost = cost(state)

    for i in range(n):
        for j in range(i + 1, n):
            neighbour = list(state)
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbour = tuple(neighbour)

            neighbour_cost = cost(neighbour)

            if neighbour_cost < best_cost:
                best = neighbour
                best_cost = neighbour_cost

    return best


def hill_climbing(initial):
    current = tuple(initial)

    print("INITIAL STATE:")
    display(current)
    print("Initial cost:", cost(current))

    while True:
        neighbour = best_successor(current)

        if cost(neighbour) >= cost(current):
            break

        current = neighbour

        print("\nCurrent State:")
        display(current)
        print("Cost:", cost(current))

        if cost(current) == 0:
            print("\nFINAL STATE:")
            display(current)
            print("Solution Success!")
            return current

    print("\nNo better neighbour found.")
    print("Final state reached:")
    display(current)
    print("Final cost:", cost(current))
    print("Solution not found by hill climbing.")
    return current



initial_state = (0, 1, 2, 3)

print("4-QUEENS PROBLEM")
solution = hill_climbing(initial_state)
