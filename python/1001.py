from math import sqrt

integers = []
while True:
    try:
        line = input()
        for word in line.split():
            integers.append(int(word))
    except EOFError:
        break
while integers:
    print("{:.4f}".format(sqrt(integers.pop())))
