from startup_profit import calculate_profit


def test_asserts_list(testing_function, asserts_list):
    print(f'Testing "{testing_function.__name__}"')

    for i, assert_data in enumerate(asserts_list):
        assert_input = assert_data[0]
        expected = assert_data[1]

        print(f'Test {i}; assert_input: {assert_input}; expected: {expected}')

        fact = testing_function(*assert_input)

        assert fact == assert_data[1], f'Test {i} failed; fact: {fact}'

    print('Tests passed')


asserts_list = [
    [[21, 108, 1], 216],
    [[5, 12, 4], -1],
    [[29420920, 98069736, 69929], -1]
]

test_asserts_list(calculate_profit, asserts_list)
