from commentator import count_goals_for_victory


def test_asserts_list(testing_function, asserts_list):

    for i, assert_data in enumerate(asserts_list):
        assert_input = assert_data[0]
        expected = assert_data[1]

        print(f'Test {i}; assert_input: {assert_input}; expected: {expected}')

        fact = testing_function(*assert_input)

        assert fact == assert_data[1], f'Test {i} failed; fact: {fact}'

    print('Tests passed')


asserts_list = [
    [['0:0', '0:0', '1'], 1],
    [['0:2', '0:3', '1'], 5],
    [['0:2', '0:3', '2'], 6],
    [['0:0', '0:0', '2'], 1],
    [['2:2', '3:3', '1'], 0],
    [['2:2', '3:3', '2'], 1],
    [['5:0', '0:5', '2'], 1],
    [['5:0', '0:5', '1'], 1],
    [['1:0', '0:0', '1'], 0],
    [['1:3', '1:0', '1'], 2],
    [['3:2', '0:2', '2'], 1]
]

test_asserts_list(count_goals_for_victory, asserts_list)
