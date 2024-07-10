def final(n, moves):
    x, y = 1, 1
    
    for move in moves:
        if move == "S":
            x = x - 1 if x > 1 else x
        elif move == "N":
            x = x + 1 if x < n else x
        elif move == "E":
            y = y + 1 if y < n else y
        elif move == "W":
            y = y - 1 if y > 1 else y
    
    return (y, x)

# Example usage:
n = 7
moves = "NNNNNNNNNNEE"  # or ["N"] * 9 + ["E"] * 2
print(final(n, moves))  # Output: (3, 7)
