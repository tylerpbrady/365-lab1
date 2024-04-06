import sys


def get_data():
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

"""
Given a student's last name, find the student's grade, classroom and teacher
If there is more than one student with the same last name, find this information for all students
"""
def option_s(data, last_name):

    desired_students = []
    for entry in data:
        # print(entry)
        if entry["StLastName"] == last_name:
            # print("found")
            desired_students.append(entry)

    print(desired_students)
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
        
        print(f"{student['StFirstName'].capitalize()} {student['StLastName'].capitalize()}, who ", end = "")        
        
        if (rides_bus == True):
            print(f"takes bus route {student['Bus']}, is a ", end = "")
        else:
            print("does not take the bus, is a ", end = "")
        
        if (k == True):
            print(f"kindergarten ", end = "")
        else:
            print(f"grade {student['Grade']} ", end = "")

        print(f"student assigned to the class of {student['TFirstName'].capitalize()} " +
              f"{student['TLastName'].capitalize()} in the classroom {student['Classroom']}. " + 
              f"{student['StFirstName'].capitalize()} has a GPA of {student['GPA']}.")


    

def option_t():
    pass

def option_b():
    pass

def option_g():
    pass

def option_a():
    pass

def option_i():
    pass

def option_q():
    pass

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
    option_s(data, "KREESE")





menu()