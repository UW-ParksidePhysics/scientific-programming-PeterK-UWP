"""
Today was another snow day, so we covered some questions regauring the homework over Microsoft Teams

we did the stars sorting problem
# formatting:
# %-19s,:
# % we are formatting
# - align to the margin
# 19s, 19 spaces then comma
"""
data = [                                          # data of stars to sort
    ('Alpha Centauri A', 4.3, 0.26, 1.56),
    ('Alpha Centauri B', 4.3, 0.077, 0.45),
    ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
    ("Barnard's Star", 6.0, 0.00004, 0.0005),
    ('Wolf 359', 7.7, 0.000001, 0.00002),
    ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
    ('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
    ('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
    ('Sirius A', 8.6, 1.00, 23.6),
    ('Sirius B', 8.6, 0.001, 0.003),
    ('Ross 154', 9.4, 0.00002, 0.0005),
]


def print_table(data, mykey):  # function to sort data based on input mykey (lambda)
    print('-------------------------------------------------------------')
    print(('%-19s, %13s, %13s, %13s') % ('Star name', 'd_sun', 'Brightness', 'Luminosity'))
    print('-------------------------------------------------------------')
    for row in sorted(data, key=mykey):
        print(('%-19s %13f %13f %13f') % row)
    print('-------------------------------------------------------------\n')


print('Sorted by star name')
print_table(data, lambda a: a[0])  # lambda does all the work here, very complicated look into book or
                                   # online for details

print('Sorted by distance to sun')
print_table(data, lambda a: a[1])

print('Sorted by brightness')
print_table(data, lambda a: a[2])

print('Sorted by luminosity')
print_table(data, lambda a: a[3])
