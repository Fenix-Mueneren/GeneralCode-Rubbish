## Author Fenix Mueneren

input_file = open("advent calendar/inputs/day3input.txt", "r")
content = input_file.read()
binary = content.split("\n")
input_file.close()

t_binary = [''.join(s) for s in zip(*binary)] # Don't ask me how, this fucking transposes the strings. Awesome.

Grate = "" 
Erate = ""
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

print("First stage of challenge")
print("Ganma Rate " + str(int(Grate, 2)))
print("Epsilon Rate " + str(int(Erate, 2)))
print("Power Consumption " + str(int(Grate, 2)*int(Erate, 2)))

print(Grate)


oxigen = binary
co2 = binary

temporal = []
oxPos = 0
while len(oxigen) > 1 :
    oximeter = ""
    t_oxigen = [''.join(s) for s in zip(*oxigen)]
    for number in t_oxigen:
        ones = 0
        zeros = 0
        for digit in number:
            if digit == '0':
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            oximeter  += "1"
        else:
            oximeter  += "0"
    if oxPos < 12:
        for index, value in enumerate(oxigen):
            if value[oxPos] == oximeter[oxPos]:  
                temporal.append(oxigen[index])
    oxPos += 1
    oxigen = temporal
    temporal = []
    
print("Oxigen LvL " + str(oxigen))

temporal = []
coPos = 0
while len(co2) > 1 :
    co2meter = ""
    t_co2 = [''.join(s) for s in zip(*co2)]
    for number in t_co2:
        ones = 0
        zeros = 0
        for digit in number:
            if digit == '0':
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            co2meter  += "0"
        else:
            co2meter  += "1"
    if coPos < 12:
        for index, value in enumerate(co2):
            if value[coPos] == co2meter[coPos]:
                temporal.append(co2[index])
    coPos += 1
    co2 = temporal
    temporal = []

print("CO2 LVL " + str(co2))
print("Life Support Rating " + str(int(oxigen[0], 2)*int(co2[0], 2)))


#parece que no funciona; no da el valor esperado