def alpha_beta(node, depth, alpha, beta, maximizing):
    if isinstance(node, int):
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(value, alpha_beta(child, depth+1, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(value, alpha_beta(child, depth+1, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


tree = [
    [[10, 9], [14, 18]],
    [[5, 4], [50, 3]]
]

result = alpha_beta(tree, 0, float('-inf'), float('inf'), True)

print("Optimal value:", result)
