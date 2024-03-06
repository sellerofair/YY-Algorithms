import trees


asserts_list = [
    [[-5, 3, 6, 2], 12],
    [[-15, 3, -4, 2], 12],
    [[4, 3, 12, 5], 17],
    [[0, 4, 5, 3], 13],
    [[6, 7, 9, 2], 15],
    [[12, 5, 4, 3], 17]
]

for i, assert_data in enumerate(asserts_list):
    assert_input = assert_data[0]
    expected = assert_data[1]

    print(f'Test {i}; assert_input: {assert_input}; expected: {expected}')

    fact = trees.count_trees(*assert_input)

    assert fact == assert_data[1], f'Test {i} failed; fact: {fact}'

print('Tests passed')
