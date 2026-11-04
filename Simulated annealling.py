
def simulated_annealing():
    current = 2
    T = 100

    for i in range(1, 4):
        next_state = current + 1
        delta_E = next_state**2 - current**2

        if delta_E > 0:
            current = next_state
            result = "Accepted"

        print("Iteration:", i)
        print("Temperature:", T)
        print("Current State:", current)
        print("Result:", result)

        T = T * 0.5

    print("\nFinal Solution:", current)

simulated_annealing()
