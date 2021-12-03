## Author Fenix Mueneren

input_file = open("advent calendar/inputs/day3input.txt", "r")
content = input_file.read()
binary = content.split("\n")
input_file.close()

t_binary = [''.join(s) for s in zip(*binary)] # Don't ask me how, this fucking transposes the strings. Awesome.

Grate = "0" 
Erate = "0"
for number in t_binary:

    amountOfones = 0
    amountOfzeros = 0
    for digit in number:
        if digit == '0':
            amountOfzeros += 1
        else:
            amountOfones += 1
    if amountOfones > amountOfzeros:
        Grate  += "1"
        Erate  += "0"
    else:
        Grate  += "0"
        Erate  += "1"
print(int(Grate, 2))
print(int(Erate, 2))
print(int(Grate, 2)*int(Erate, 2))

