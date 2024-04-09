import sys


def get_data():
    try: 
        with open("students.txt", "r") as file:
            data = file.read()
            list = data.split("\n")
            list.pop()
            students = []
            for thing in list:
                atr_list = thing.split(",")
                entry = {"StLastName" : atr_list[0],
                        "StFirstName" : atr_list[1],
                        "Grade" : atr_list[2],
                        "Classroom" : atr_list[3],
                        "Bus" : atr_list[4],
                        "GPA" : atr_list[5],
                        "TLastName" : atr_list[6],
                        "TFirstName" : atr_list[7]}
                students.append(entry)

            return students        
    except:
        print("\nError finding file.\n")
        exit()
"""
Given a student's last name, find the student's grade, classroom and teacher
If there is more than one student with the same last name, find this information for all students
"""
def option_s(data, last_name, bus = None):

    desired_students = []
    for entry in data:
        # print(entry)
        if entry["StLastName"] == last_name:
            # print("found")
            desired_students.append(entry)

    if len(desired_students) == 0:
        print("No Student found.")
        return

    for student in desired_students:
        rides_bus = None   
        k = None

        if (student["Grade"] == "0"):
            k = True
        else:
            k = False

        if (student["Bus"] == "0"):
            rides_bus = False
        else:
            rides_bus = True
        
        print(f"{student['StLastName'].capitalize()} {student['StFirstName'].capitalize()}, ", end = "")        
        
        if (bus != None):
            if (rides_bus):
                print(f"bus route {student['Bus']}.")
            else:
                print("does not take the bus.")
        else:
            if (k == True):
                print(f"who is a kindergarten ", end = "")
            else:
                print(f"who is a grade {student['Grade']} ", end = "")

            print(f"student assigned to the class of {student['TFirstName'].capitalize()} " +
                f"{student['TLastName'].capitalize()} in the classroom {student['Classroom']}. ") 

"""
Searches and finds all students who have the teacher with the desired last name
"""
def option_t(data, last_name):

    desired_students = []
    for entry in data:
        if entry["TLastName"] == last_name:
            desired_students.append(entry)

    if len(desired_students) == 0:
        print("Either this teacher doesn't exist or they do not teach any students.")

    for student in desired_students:
        print(f"{student['StLastName'].capitalize()} {student['StFirstName'].capitalize()}")

"""
searches and finds all students taking specified bus route
"""
def option_b(data, route):

    desired_students = []
    for entry in data:
        if entry['Bus'] == route:
            desired_students.append(entry)

    if len(desired_students) == 0:
        print("No students found.")

    for student in desired_students:
        print(f"{student['StLastName'].capitalize()} {student['StFirstName'].capitalize()} ", end = "")
        if student['Grade'] == 0:
            print(f"kindergarten, classroom {student['Classroom']}")
        else:
            print(f"grade {student['Grade']}, classroom {student['Classroom']}.")

"""
searches and finds all students in specified grade level
"""
def option_g(data, grade, high_low = None):

    desired_students = []
    for entry in data:
        if entry['Grade'] == grade:
            # print(entry['GPA'])
            desired_students.append(entry)

    if high_low == "H":
        highest = float(desired_students[0]['GPA'])
        target_student = desired_students[0]
        for student in desired_students:
            if float(student['GPA']) > highest:
                highest = float(student['GPA'])
                target_student = student
        if student['Bus'] == "0":
            print(f"{target_student['StLastName'].capitalize()} {target_student['StFirstName'].capitalize()} has " +
                  f"the highest GPA being {target_student['GPA']}. They don't take the bus and their teacher is " +
                  f"{target_student['TLastName'].capitalize()} {target_student['TFirstName'].capitalize()}")
        else:
            print(f"{target_student['StLastName'].capitalize()} {target_student['StFirstName'].capitalize()} has " +
                  f"the highest GPA being {target_student['GPA']}. They take bus route {target_student['Bus']} and their teacher is " +
                  f"{target_student['TLastName'].capitalize()} {target_student['TFirstName'].capitalize()}")
    elif high_low == "L":
        lowest = float(desired_students[0]['GPA'])
        target_student = desired_students[0]
        for student in desired_students:
            if float(student['GPA']) < lowest:
                lowest = float(student['GPA'])
                target_student = student
        if target_student['Bus'] == "0":
            print(f"{target_student['StLastName'].capitalize()} {target_student['StFirstName'].capitalize()} has " +
                  f"the lowest GPA being {target_student['GPA']}. They don't take the bus and their teacher is " +
                  f"{target_student['TLastName'].capitalize()} {target_student['TFirstName'].capitalize()}")
        else:
            print(f"{target_student['StLastName'].capitalize()} {target_student['StFirstName'].capitalize()} has " +
                  f"the lowest GPA being {target_student['GPA']}. They take bus route {target_student['Bus']} and their teacher is " +
                  f"{target_student['TLastName'].capitalize()} {target_student['TFirstName'].capitalize()}")
    else:
        if len(desired_students) != 0:
            for student in desired_students:
                print(f"{student['StLastName'].capitalize()} {student['StFirstName'].capitalize()}")
        else:
            print("No students found.")
"""
Computes average GPA for specified grade
"""
def option_a(data, grade):

    desired_students = []
    for entry in data:
        if entry['Grade'] == grade:
            desired_students.append(entry)

    if len(desired_students) == 0:
        print("No students to find average for.")
        return

    total = 0
    for student in desired_students:
        total += float(student['GPA'])
    
    avg = total / len(desired_students)

    if grade == "0":
        print(f"The average GPA for kindergarten was {round(avg, 2)}.")
    else:
        print(f"The average GPA for grade {grade} was {round(avg, 2)}.")


"""
Calculates number of students in each grade
"""
def option_i(data):

    grade_list = {
        "Kindergarten" : 0,
        "Grade 1" : 0,
        "Grade 2" : 0,
        "Grade 3" : 0,
        "Grade 4" : 0,
        "Grade 5" : 0,
        "Grade 6" : 0
    }

    for student in data:
        match student['Grade']:
            case "0":
                grade_list['Kindergarten'] += 1
            case "1":
                grade_list['Grade 1'] += 1
            case "2":
                grade_list['Grade 2'] += 1
            case "3":
                grade_list['Grade 3'] += 1
            case "4":
                grade_list['Grade 4'] += 1
            case "5":
                grade_list['Grade 5'] += 1
            case "6":
                grade_list['Grade 6'] += 1
    
    sorted_students = sorted(grade_list, key = lambda x:grade_list[x])
    keys = grade_list.keys()
    # for i in range(7):
    #     print(f"{grade_list[i]}: {grade_list[str(i)]} students")
    for key in grade_list.keys():
        print(f"{key}: {grade_list[key]} students.")
        


def show_options():
    print("")
    print("S[tudent]")
    print("T[eacher]")
    print("B[us]")
    print("G[rade]")
    print("A[verage]")
    print("I[nfo]")
    print("Q[uit]")

def menu():

    data = get_data()
    # option_s(data, "HAVIR")

    while True:
        show_options()
        input_string = input("\nEnter command: ")
        user_args = input_string.split()
        # S: CORKER 

        match user_args[0]:
            case "S:" | "Student:":
                
                if (len(user_args) == 1):
                    print("\nInvalid input.")
                    continue
                elif (len(user_args) == 2):
                    print("")
                    option_s(data, user_args[1])
                elif (len(user_args) == 3) and (user_args[2] == "B" or user_args[2] == "Bus"):
                    print("")
                    option_s(data, user_args[1], True)
                else:
                    print("\nInvalid input.")
                    continue

            case "T:" | "Teacher:":

                if (len(user_args) == 1):
                    print("\nInvalid Input.")
                    continue
                elif (len(user_args) == 2):
                    print("")
                    option_t(data, user_args[1])
                else:
                    print("\nInvalid Input.")
                    continue
                
            case "B:" | "Bus:":
                
                if (len(user_args) == 1):
                    print("\nInvalid Input.")
                    continue
                elif (len(user_args) == 2):
                    print("")
                    option_b(data, user_args[1])

            case "G:" | "Grade:":
                
                if (len(user_args) == 1):
                    print("\nInvalid Input")
                    continue
                elif (len(user_args) == 2):
                    print("")
                    option_g(data, user_args[1])
                elif (len(user_args) == 3):
                    print("")
                    option_g(data, user_args[1], user_args[2])
                else:
                    print("\nInvalid Input.")
                    continue

            case "A:" | "Average:":

                if (len(user_args) == 1):
                    print("\nInvalid Input")
                    continue
                elif (len(user_args) == 2):
                    print("")
                    option_a(data, user_args[1])
                else:
                    print("\nInvalid Input.")
                    continue

            case "I" | "Info":
                
                if (len(user_args) != 1):
                    print("\nInvalid Input.")
                    continue
                else:
                    print("")
                    option_i(data)

            case "Q" | "Quit":

                print("\nProgram exiting.")
                break

            case _:

                print("\nInvalid choice.")
                continue



"""

the test file is a text file of what your expected outputs are and then
the output file is a text file of you copy and pasting the actual outputs of your functions

"""

menu()

"""

S - done
T - done
B - done
G - done
A - done

"""