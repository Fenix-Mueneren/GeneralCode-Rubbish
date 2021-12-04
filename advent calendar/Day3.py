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

def commonbit(pos, data):
    zeroCount = 0
    oneCount = 0
    for value in data:
        if int(value[pos]) == 0:
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        return 0
    elif zeroCount < oneCount:
        return 1
    else:
        return 2 # This means equal 1's and 0's, so the decision to which number keep should be taken another way.

oxigen = binary
temporal = []
pos = 0
while len(oxigen) > 1:
    bit = commonbit(pos, oxigen)
    if bit == 2:
        for value in oxigen:
            if int(value[pos]) == 1:
                temporal.append(value)
    elif bit == 1:
        for value in oxigen:
            if int(value[pos]) == 1:
                temporal.append(value)
    elif bit == 0:
        for value in oxigen:
            if int(value[pos]) == 0:
                temporal.append(value)
    oxigen = temporal
    temporal = []
    pos +=1

print("Oxigen Level " + str(int(oxigen[0], 2)))

co2 = binary
temporal = []
pos = 0
while len(co2) > 1:
    bit = commonbit(pos, co2)
    if bit == 2:
        for value in co2:
            if int(value[pos]) == 0:
                temporal.append(value)
    elif bit == 1:
        for value in co2:
            if int(value[pos]) == 0:
                temporal.append(value)
    elif bit == 0:
        for value in co2:
            if int(value[pos]) == 1:
                temporal.append(value)
    co2 = temporal
    temporal = []
    pos +=1

print("Co2 Level " + str(int(co2[0], 2)))

print("Life Support Status "+ str(int(co2[0],2)*int(oxigen[0],2)))