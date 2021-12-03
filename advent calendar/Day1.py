## Author Fenix Mueneren

largemeasurements = 0

input_file = open("advent calendar/inputs/day1input.txt", "r")
content = input_file.read()

values = content.split("\n")
input_file.close()

for index, value in enumerate(values):
    if index-1 >= 0 :
        if int(value) > int(values[index-1]):
                largemeasurements += 1
    
print(largemeasurements)

largerwindows = 0
for index, value in enumerate(values):
    if index < len(values)-3 :
        windowA = int(values[index]) + int(values[index+1]) + int(values[index+2])
        windowB = int(values[index+1]) + int(values[index+2]) + int(values[index+3])
        if windowB > windowA:
                largerwindows += 1
    
print(largerwindows)