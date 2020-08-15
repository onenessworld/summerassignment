time_table_dict = {}
line_counter_value = 0
number_of_people = 0
time_start_key = 0
time_end = 0
min_points = 0
min_points_person = None
points_dict = {}
input_file = open("9.in")

number_of_people = int(input_file.readline())
line_counter_value = line_counter_value + 1
for line in input_file:
    #print(line)
    time_start_key, time_end = line.split()
    time_start_key = int(time_start_key)
    time_end = int(time_end)
    #print(time_start_key, time_end)
    #Writing the timetable dictionary
    for start_time in range(time_start_key, time_end):
        if start_time in time_table_dict:
            time_table_dict[start_time] = [] #means many people
        else :
            time_table_dict[start_time] = [line_counter_value]

    line_counter_value = line_counter_value + 1

#Display Dict and print values(people) list of size =1 
#print(time_table_dict)
for time_start_key in time_table_dict:
    #print(time_start_key,time_table_dict[time_start_key])
    if len(time_table_dict[time_start_key]) == 1:
        key_in_points_dict = time_table_dict[time_start_key][0] #read the list element zero
        if key_in_points_dict in points_dict:
            points_dict[key_in_points_dict] = points_dict[key_in_points_dict] + 1
        else :
            points_dict[key_in_points_dict] = 1
#print(points_dict)

for person in range(1,(number_of_people+1)):
    if person not in points_dict:
        min_points_person = person
        min_points = 0
        break
    else:
        if points_dict[person] < min_points or min_points_person == None:
            min_points = points_dict[person]
            min_points_person = person
#print(min_points_person,min_points)
#print("Fired %s" % min_points_person)

#Coverage Max

total_coverage = len(time_table_dict)
final_coverage = total_coverage - min_points
print(final_coverage)

