from bishops_and_rooks import count_safe_cages


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
    [
        [[
            '********',
            '********',
            '*R******',
            '********',
            '********',
            '********',
            '********',
            '********'
        ]],
        49
    ],
    [
        [[
            '********',
            '********',
            '******B*',
            '********',
            '********',
            '********',
            '********',
            '********'
        ]],
        54
    ],
    [
        [[
            '********',
            '*R******',
            '********',
            '*****B**',
            '********',
            '********',
            '********',
            '********'
        ]],
        40
    ],
    [
        [[
            '********                                      *',
            '********      ',
            '********                  ',
            '********       ',
            '********       ',
            '********        ',
            '********             ',
            '********   ',
            '                                 ',
            '  ',
            ''
        ]],
        64
    ],
    [
        [[
            'R******R',
            '********',
            '********',
            '********',
            '********',
            '********',
            '********',
            'R******R'
        ]],
        36
    ],
    [
        [[
            'B******B',
            '********',
            '********',
            '********',
            '********',
            '********',
            '********',
            'B******B'
        ]],
        48
    ],
    [
        [[
            '********',
            '***B****',
            '**BRB***',
            '***B****',
            '********',
            '********',
            '********',
            '********'
        ]],
        41
    ],
    [
        [[
            '********',
            '********',
            '***R****',
            '****B***',
            '********',
            '********',
            '********',
            '********'
        ]],
        40
    ]
]

test_asserts_list(count_safe_cages, asserts_list)
