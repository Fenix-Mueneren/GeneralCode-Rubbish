## Author Fenix Mueneren


input_file = open("advent calendar/inputs/day2input.txt", "r")
content = input_file.read()

plottedcourse = content.split("\n")
input_file.close()
horizontal = 0 
depth = 0


for step in plottedcourse :
    course = step.split(" ")
    if (course[0]) == "forward":
        horizontal += int(course[1])
    elif (course[0]) == "up":
        depth -= int(course[1])
    elif (course[0]) == "down":
        depth += int(course[1])

print("First part of the challenge " + str(depth * horizontal))

horizontal = 0 
depth = 0
aim = 0

for step in plottedcourse :
    course = step.split(" ")
    if (course[0]) == "forward":
        horizontal += int(course[1])
        depth += aim*int(course[1])
    elif (course[0]) == "up":
        aim -= int(course[1])
    elif (course[0]) == "down":
        aim += int(course[1])
        

print("Seccond part of the challenge " + str(depth * horizontal))