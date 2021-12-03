## Author Fenix Mueneren

largemeasurements = 0

input_file = open("advent calendar/inputs/day1input.txt", "r")
content = input_file.read()

values = content.split("\n")
input_file.close()

for index, value in enumerate(values):
    if index-1 >= 0 :
        if value > values[index-1]:
                largemeasurements += 1
    
print(largemeasurements)
