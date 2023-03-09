"""
Today is a Q/A session: ask me homework problems or other general questions you may have


Some Logistics/Navigation:
To test things in the Terminal, click terminal
->type: C:\Python37\python.exe<filename>

To test things in the shell, click python console
-> right click file to test
-> refactor -> convert to Python Package
-> type in the shell: import <filename>

"""
import sys

try:
    F = float(sys.argv[1])  #[0] filename, [1] value
    C = (F - 32) * (5 / 9)
    print(C, "celsius")

except IndexError:
    print('Error')
