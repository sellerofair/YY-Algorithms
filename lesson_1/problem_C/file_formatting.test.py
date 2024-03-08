import file_formatting


def test_asserts_list(testing_function, asserts_list):

    for i, assert_data in enumerate(asserts_list):
        assert_input = assert_data[0]
        expected = assert_data[1]

        print(f'Test {i}; assert_input: {assert_input}; expected: {expected}')

        fact = testing_function(*assert_input)

        assert fact == assert_data[1], f'Test {i} failed; fact: {fact}'

    print('Tests passed')


asserts_list = [
    [[1], 1],
    [[4], 1],
    [[12], 3],
    [[9], 3],
    [[0], 0],
    [[5], 2],
    [[7], 3],
    [[6], 3]
]

test_asserts_list(file_formatting.count_keystrokes_in_string, asserts_list)

asserts_list = [
    [[[1, 4, 12, 9, 0]], 8]
]

test_asserts_list(file_formatting.count_keystrokes, asserts_list)
