from math_operations import is_odd, count_odd_numbers, find_operations


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
    [[2], False],
    [[0], False],
    [[1], True],
    [[-5], True],
    [[-6], False]
]

test_asserts_list(is_odd, asserts_list)


asserts_list = [
    [[[5, 7, 2]], 2],
    [[[4, -5]], 1],
    [[[4, -5, 0, 12, 1345, 11, -602, -909]], 4]
]

test_asserts_list(count_odd_numbers, asserts_list)


asserts_list = [
    [[[5, 7, 2]], 'x+'],
    [[[4, -5]], '+'],
    [[[4, -5, 0, 12, 1345, 11, -602, -909]], 'x++++++'],
    [[[390029247, 153996608, -918017777]], 'x+']
]

test_asserts_list(find_operations, asserts_list)
