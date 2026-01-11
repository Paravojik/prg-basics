def f(value1):
    def inner(value2):
        return value1 * value2
    return inner

if __name__ == "__main__":
    times_five = f(5)
    print(times_five(8))   # Expected: 40

    times_three = f(3)
    print(times_three(7))  # Expected: 21