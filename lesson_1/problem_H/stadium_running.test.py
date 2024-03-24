from stadium_running import run_around_stadium


def test_asserts_list(testing_function, asserts_list):
    print(f'Testing "{testing_function.__name__}"')

    for i, assert_data in enumerate(asserts_list):
        assert_input = assert_data[0]
        expected = assert_data[1]

        print(f'Test {i}; assert_input: {assert_input}; expected: {expected}')

        fact = list(testing_function(*assert_input))

        assert fact == expected, f'Test {i} failed; fact: {fact}'

    print('Tests passed')


asserts_list = [
    [[6, 3, 1, 1, 1], [True, 1]],
    [[12, 8, 10, 5, 20], [True, 0.3]],
    [[5, 0, 0, 1, 2], [True, 2]],
    [[10, 7, -3, 1, 4], [True, 0.8571428571]],
    [[10, 2, 0, 1, 0], [False, None]]
]

test_asserts_list(run_around_stadium, asserts_list)
