from barracks_destruction import destruct_barracks


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
    [[10, 11, 15], 4],
    [[1, 2, 1], -1],
    [[1, 1, 1], 1],
    [[25, 200, 10], 13],
    [[250, 500, 187], -1]
]

test_asserts_list(destruct_barracks, asserts_list)
