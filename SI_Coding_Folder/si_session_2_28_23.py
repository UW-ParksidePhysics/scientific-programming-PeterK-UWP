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

