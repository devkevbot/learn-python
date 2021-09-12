def run_test(fn: function, inputs: list) -> None:
    longest_input = find_longest_test_case_input(inputs)
    ljust_amount = max(25, 2 * longest_input)

    for test in inputs:
        *params, expected = test
        result = fn(*params)

        param_str = list(params)
        input_str = f"TEST: {param_str}".ljust(ljust_amount)
        status_str = (
            f"FAILED:  GOT {result}, EXPECTED: {expected}"
            if result != expected
            else "OK"
        )

        print(f"{input_str} ... {status_str}")


def find_longest_test_case_input(inputs: list) -> None:
    longest_input = 0
    for test in inputs:
        input_length = sum(len(s) for s in test[0 : len(test) - 1])
        longest_input = max(longest_input, input_length)
    return longest_input
