"""
Today we will cover the __main__ function:
This function essentially is your run command, things not in the main function will not run.
Great way to debug and test files as well as making the code look neat if done properly

Using the code from session 2/9/23 we will make this into a def statement and then into a main function.
"""
from functions_2_28_23 import running_chicken, bruh_moment
from si_session_2_9_23 import convert_seconds_to_years

if __name__ == "__main__":
    # sentence run
    adjective = input('input a past-tense adjective:')
    print(running_chicken(adjective))
    # computation
    seconds = eval(input('input seconds'))
    print(f'converting {seconds} seconds to years')
    print(f'{seconds} equate to {convert_seconds_to_years(seconds)} years')
    # sentence bruh
    anything = input('input anything:')
    print(bruh_moment(anything))

# other:
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




