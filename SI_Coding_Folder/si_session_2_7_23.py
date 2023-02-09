"""
Today we will cover some basics to coding in python which include:
 - formatting print statements
 - definition statements
 - for loops
 - using loops to graph
"""

# formatting print statements

# variable (greeting), assigned to a string (Hello World)
greeting = 'Hello World'
print(greeting)

# f - string
print(f'{greeting}')

print(f'Now I can say {greeting} in a f - string!')

statement_1 = 'Now I can say'
statement_2 = 'in a f - string!'

print(f'{statement_1} {greeting} {statement_2}')

m = eval(input('type in a mass:'))             # mass         kg
a = eval(input('type in an acceleration:'))    # acceleration  m/s/s


# definition statement
def force(mass, acceleration):
    f = mass * acceleration
    return f


print(force(m, a))
print(f'Given a mass: {m}kg, and an acceleration: {a}m/s/s, we get a force: {force(m, a)}N!')



