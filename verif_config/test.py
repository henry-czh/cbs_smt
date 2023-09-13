import os


path = os.path.dirname(__file__)
print(path)

path = os.path.abspath(__file__)
print(path)
path = os.path.dirname(path)
print(path)

