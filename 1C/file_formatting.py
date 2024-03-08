TABS_COUNT = 4

def count_key_clicks_in_string(string_length):
    tab_key_clicks_count = 0

def count_key_clicks(strings_lengths_list):
    key_clicks_count = 0
    for string_length in strings_lengths_list:
        key_clicks_count += count_key_clicks_in_string(string_length)

    return key_clicks_count

if __name__ == '__main__':
    strings_count = int(input())
    strings_lengths_list = [int(n) for n in input().split()]

    print(count_key_clicks(strings_lengths_list))
