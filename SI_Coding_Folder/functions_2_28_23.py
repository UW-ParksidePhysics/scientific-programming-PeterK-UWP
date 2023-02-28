"""
Given code to output
"""


def running_chicken(word):
    sentence = f'the running chicken was {word} into oblivion'
    return sentence


def bruh_moment(word):
    sentence = f'{word}, that was a bruh moment'
    return sentence

"""
4.1 homework
"""
fahrenheit_temp = eval(input('input temperature in fahrenheit:'))


def f_to_c(f):
    c = 5/9 * (f - 32)
    return c

"""
4.4 homework
"""
"""
Temperature data
----------------
Fahrenheit degrees: 67.2
"""


data_array = open('filename.txt', 'r')
data_contents = data_array.readlines()
data_array.close()

f_value = int(data_contents[2].split()[2])

print(f'{f_to_c(f_value)}')