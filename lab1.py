import sys


def get_data():
    with open("test.txt", "r") as file:
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

def option_s():
    pass

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





lst = get_data()
print(lst)