"""
A recursive definition to calculate the value f.
"""
def f(a, b, c, d):
    if a == b == c == d == 0:
        return 1
    print(f"STEP: ({abs(a - b)}, {abs(b - c)}, {abs(c - d)}, {abs(d - a)})") 
    return 1 + f(abs(a - b), abs(b - c), abs(c - d), abs(d - a))

"""
Checks if a set of inputs has affinity with 0.
x[0] is always 0 and x[3] is always the largest value. Therefore, x[1] + x[2] must equal x[3].
"""
def is_valid(x):
    return x[1] + x[2] == x[3]

"""
Moves a set of inputs up a layer.
"""
def go_up(a, b, c, d):
    return (0, a, d - c, d)

bound = 10_000_000

x = (1, 1, 1, 1)
while True:
    new = go_up(x[0], x[1], x[2], x[3])

    if not is_valid(new):
        last = new

        # Checking if all elements are even
        if (new[0] + new[1] + new[2] + new[3]) % 2 == 1:
            new = (new[0] * 2, new[1] * 2, new[2] * 2, new[3] * 2)

        # Translating by the factor
        k = int((new[3] - new[2] - new[1]) / 2)

        # Reassigning
        new = (new[0] + k, new[1] + k, new[2] + k, new[3] + k)

    # Checking if we have surpassed the bound on d (which will be the largest)
    if new[3]> bound:
        print(f"Final Result: {last}")
        exit()

    # Continuing the process
    x = new
    print(f"Step: {x}")
