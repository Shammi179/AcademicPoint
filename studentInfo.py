import sqlite3
import create_tables
from colorama import Fore
import getpass


import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')



#Connect to db
conn=sqlite3.connect('StudentInfo.db')

#create cursor
c=conn.cursor()

create_tables



"""Student Panel"""

def studentMenu(sID):
    while True:
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t\t   #########  STUDENT PANEL  #########\n')
        print(Fore.RESET)
        print("""\t\t\t\t\t\t[1] Student Profile
        \t\t\t\t\t[2] Registered Courses\n\t\t\t\t\t\t[3] Department Information
        \t\t\t\t\t[4] Search Teacher\n\t\t\t\t\t\t[5] Result
        \t\t\t\t\t[6] Library Information\n\t\t\t\t\t\t[7] Book Information\n\n""")

        admin= input(Fore.CYAN+'\t\t\t\t\t\tEnter Your Choice: ')
        print(Fore.RESET)

        if admin=='1': studentProfile(sID)
        elif admin=='2': semCourses(sID)
        elif admin=='3': deptInfo()
        elif admin=='4': searchTeacher()
        elif admin=='5': result()
        elif admin=='6': libraryInfo(sID)
        elif admin=='7': bookInfo()
        elif admin=='q': exit()


def studentProfile(sID):
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t        ########  STUDENT PROFILE  ########\n')
        print(Fore.RESET)
        c.execute("SELECT * FROM student WHERE studentID = ?",(sID,))
        sInfo = c.fetchall()
        print(f"{sInfo[0][2]}'s Profile:\n\n")
        print(f'Your Student ID: {sInfo[0][0]}')
        print(f'Name: {sInfo[0][2]}')
        print(f"Father's Name: {sInfo[0][4]}")
        print(f"Mother's Name: {sInfo[0][5]}")
        print(f'Email: {sInfo[0][1]}')
        print(f'Mobile: {sInfo[0][7]}')
        print(f'Gender: {sInfo[0][3]}')
        print(f'Address: {sInfo[0][6]}')
        print(f'Department ID: {sInfo[0][8]}')
        print(f'Batch: {sInfo[0][9]}')

        print('Edit your Profile: \n\n\t\t\t[1] Change Mobile\t[2] Change Address\t[3] Change Password\n\n')
        choice = input("Enter your choice or 'q' for menu: ")
        if choice == '1': 
            nMobile = input("Enter your new Mobile Number: ")
            c.execute('UPDATE student SET cell = ? WHERE studentID = ?',(nMobile,sID,))
            print('Your Mobile Number Updated !')
            input("Press any key to go Updated Profile ...")
        elif choice == '2': 
            nAddress = input("Enter your new Address: ")
            c.execute('UPDATE student SET address = ? WHERE studentID = ?',(nAddress,sID,))
            print('Your Address Updated !')
            input("Press any key to go Updated Profile ...")
        elif choice =='3': changePass(sID)
        else: break
    conn.commit()





def semCourses(sID):
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t\t   #########  REGISTERED COURSES #########\n') 
        print(Fore.RESET)
        semester = input("\nSearch by Semester (Fall-20): ")
        c.execute("SELECT * FROM registeredCourse WHERE studentID = ? AND semester = ?",(sID,semester,))
        scInfo = c.fetchall()
        if len(scInfo)>=1: 
            print(f'Your Registered Courses of Semester {semester}:\n\n')
            for i in range(len(scInfo)): 
                print(f'Course Code: {scInfo[i][1]}')
                c.execute("SELECT * FROM course WHERE courseCode = ?",(scInfo[i][1],))
                cInfo = c.fetchall()
                print(f'Course Title: {cInfo[0][1]}')
                print(f'Course Credit: {cInfo[0][2]}')
                print(f'Section: {scInfo[i][3]}')
                c.execute("SELECT * FROM teacher WHERE teacherID = ?",(scInfo[i][4],))
                tInfo = c.fetchall()
                print(f'Teacher Name: {tInfo[0][2]}')

        else: 
            print(f'Not Registered Yet!')
        
        another = input("\n\nSearch Again? Press 'y' or 'q' for menu: ")
    conn.commit()



def result():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t\t   #########  RESULT OF SEMESTER #########\n') 
        print(Fore.RESET)
        studentID = input('\nStudent ID (191-15-12345): ')
        semester = input("Search by Semester (Fall-20): ")

        c.execute("SELECT * FROM result WHERE studentID = ? AND semester = ?",(studentID,semester,))
        scInfo = c.fetchall()
        totalCourse = 0
        totalResult = 0
        if len(scInfo)>=1: 
            print(f'Result of {studentID}, {semester}:\n\n')
            for i in range(len(scInfo)): 
                print(f'Course Code: {scInfo[i][1]}')
                c.execute("SELECT * FROM course WHERE courseCode = ?",(scInfo[i][1],))
                cInfo = c.fetchall()
                print(f'Course Title: {cInfo[0][1]}')
                print(f'Course Credit: {cInfo[0][2]}')
                print(f'Grade Point: {scInfo[i][3]}')
                totalCourse +=1
                totalResult +=scInfo[i][3]
            print(f'\n\nResult in SGPA: {totalResult/totalCourse}')
        else: 
            print(f'Result is not Published!')
        
        another = input("\n\nSearch Again? Press 'y' or 'q' for menu: ")
    conn.commit()






def libraryInfo(sID):
    screen_clear()
    print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
    print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
    print('\n\t\t\t\t\t   #########  LIBRARY INFORMATION #########\n') 
    print(Fore.RESET)
    c.execute("SELECT * FROM library WHERE studentID = ? ORDER BY Taken DESC",(sID,))
    lInfo = c.fetchall()
    if len(lInfo)>=1: 
        print(f"\n\nYour Latest Library Information: \n")
        for i in range(len(lInfo)): 
            print(f'\tBook ID: {lInfo[i][1]}')
            c.execute("SELECT * FROM book WHERE bookID = ?",(lInfo[i][1],))
            bInfo = c.fetchall()
            print(f'\tBook Name: {bInfo[0][1]}')
            print(f'\tBook Category: {bInfo[0][2]}')
            print(f'\tTaken Date: {lInfo[i][2]}')
            print(f'\tReturn Date: {lInfo[i][3]}\n\n')
    else: 
        print(f'No book has been taken by you!')
    
    input("\n\nPress any key for menu: ")
    conn.commit()



def searchTeacher():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t\t   #########  TEACHER INFORMATION #########\n') 
        print(Fore.RESET)
        tName = input("\nSearch by Teacher Name or Initial : ")
        c.execute("SELECT * FROM teacher WHERE tName LIKE ? OR tInitial LIKE ?",('%'+tName+'%','%'+tName+'%',))
        tInfo = c.fetchall()
        if len(tInfo)>=1: 
            for i in range(len(tInfo)): 
                print(f"\n\nTeacher's ID: {tInfo[i][0]}")
                print(f'Name: {tInfo[i][2]}')
                print(f'Initial: {tInfo[i][3]}')
                print(f'Email: {tInfo[i][1]}')
                print(f'Designation: {tInfo[i][4]}')
                c.execute("SELECT * FROM department WHERE deptID = ?",(tInfo[i][5],))
                dInfo = c.fetchall()
                print(f'Department: {dInfo[0][1]}')
        else: 
            print(f'Not found!')
        
        another = input("\n\nSearch Again? Press 'y' or 'q' for menu: ")
    conn.commit()







"""Teacher Panel"""

def teacherMenu(tID):
    while True:
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t\t   #########  TEACHER PANEL #########\n')
        
        print(Fore.RESET)
        print("""\t\t\t\t\t\t[1] Teacher Profile
        \t\t\t\t\t[2] Course Information\n\t\t\t\t\t\t[3] Department Information
        \t\t\t\t\t[4] Book Information\n\n""")

        admin= input(Fore.CYAN+'\t\t\t\t\t\tEnter Your Choice: ')
        print(Fore.RESET)

        if admin=='1': teacherProfile(tID)
        elif admin=='2': courseInfo()
        elif admin=='3': deptInfo()
        elif admin=='4': bookInfo()
        elif admin=='q': exit()




def teacherProfile(tID):
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t        ########  TEACHER PROFILE  ########\n')
        print(Fore.RESET)
        c.execute("SELECT * FROM teacher WHERE teacherID = ?",(tID,))
        tInfo = c.fetchall()
        print(f"{tInfo[0][2]}'s Profile:\n\n")
        print(f'Your Employee ID: {tInfo[0][0]}')
        print(f'Name: {tInfo[0][2]}')
        print(f'Email: {tInfo[0][1]}')
        print(f'Mobile: {tInfo[0][6]}')
        print(f'Teacher Initial: {tInfo[0][3]}')
        print(f'Designation: {tInfo[0][4]}')
        print(f'Department ID: {tInfo[0][5]}')

        print('Edit your Profile: \n\n\t\t\t[1] Change Mobile\t[2] Change Password\n\n')
        choice = input("Enter your choice or 'q' for menu: ")
        if choice == '1': 
            nMobile = input("Enter your new Mobile Number: ")
            c.execute('UPDATE teacher SET cell = ? WHERE teacherID = ?',(nMobile,tID,))
            print('Your Mobile Number Updated !')
            input("Press any key to go Updated Profile ...")
        elif choice =='2': changePass(tID)
        else: break
    conn.commit()



def changePass(uID):
    while True:
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t        ########  CHANGE PASSWORD  ########\n')
        print(Fore.RESET)
        c.execute("SELECT * FROM user WHERE userID = ?",(uID,))
        uInfo = c.fetchall()
        cPass = getpass.getpass("Enter your Current Password: ")
        if uInfo[0][1] == cPass:
            nPass = getpass.getpass("Enter your New Password: ")
        else: 
            print('Current Password not matched!\n')
            input('Press Any to Try Again ...')
            continue

        c.execute("UPDATE user SET uPass = ? WHERE userID = ?",(nPass,uID,))
        print('Your Password Succesfully Changed !')
        conn.commit()
        input('Press Any to go Profile ...')
        break
        
        





def deptInfo():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t        ########  DEPARTMENT INFORMATION  ########\n')
        print(Fore.RESET)
        
        dept = input("\nSearch by short form of Dept. : ")
        c.execute("SELECT * FROM department WHERE dName LIKE ?",('%'+dept+'%',))
        dInfo = c.fetchall()
        if len(dInfo)>=1: 
            print(f'\n\nDepartment Name: {dInfo[0][1]}')
            print(f'Department ID: {dInfo[0][0]}')
        else: 
            print(f'\nNot found!')
        
        another = input("\n\nSearch Again? Press 'y' or 'q' for menu: ")
    conn.commit()





def bookInfo():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t          #########  BOOK INFORMATION  ##########\n')
        print(Fore.RESET)
        bookName = input("\nSearch by Book Name : ")
        c.execute("SELECT * FROM book WHERE bName LIKE ?",('%'+bookName+'%',))
        bInfo = c.fetchall()
        if len(bInfo)>=1: 
            for i in range(len(bInfo)): 
                print(f'\n\nBook Name: {bInfo[i][1]}')
                print(f'Book ID: {bInfo[i][0]}')
                print(f'Book Category: {bInfo[i][2]}')
        else: 
            print(f'Not found!')
        
        another = input("\n\nSearch Again? Press 'y' or 'q' for menu: ")
    conn.commit()





def courseInfo():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t          #######  COURSE INFORMATION  ########\n')
        print(Fore.RESET)
        courseName = input("\nSearch by Course Title or Code: ")
        c.execute("SELECT * FROM course WHERE CourseTitle LIKE ? OR courseCode LIKE ?",('%'+courseName+'%','%'+courseName+'%',))
        cInfo = c.fetchall()
        if len(cInfo)>=1: 
            for i in range(len(cInfo)): 
                print(f'\n\nCourse Code: {cInfo[i][0]}')
                print(f'Course Title: {cInfo[i][1]}')
        else: 
            print(f'Not found!')
        
        another = input("\n\nSearch Again? Press 'y' or 'q' for menu: ")
    conn.commit()






"""Login"""

def login():
    screen_clear()
    print(Fore.CYAN+"""
\t\t\t     _                 _                _        ____       _       _   
\t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
\t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
\t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
\t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
    print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
    print('\n\t\t\t\t       #########  LOGIN TO YOUR ACCOUNT  ##########\n\n')
    print(Fore.RESET)
    userID=input('\t\tEnter your User ID: ')
    uPass=getpass.getpass('\t\tEnter your Password: ')
    c.execute("SELECT isStudent, isTeacher FROM user WHERE userID = ? AND uPass = ?",(userID,uPass,))
    lInfo = c.fetchall()
    if len(lInfo)<1:
        print('\nLogin Failed!!!\nCheck your Login Credentials.')
        input("Press Any key to Try Again: ")
        login()
    elif lInfo[0][0] == 1:
        studentMenu(userID)
    elif lInfo[0][1] == 1:
        teacherMenu(userID)
    else:
        adminPanel()




"""Admin Panel"""

def adminPanel():

    while True:
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t         ############  ADMIN PANEL  #############\n')
        print(Fore.RESET)
        print("""\t\t\t\t\t\t[1] Registration Information
        \t\t\t\t\t[2] Library Information\n\t\t\t\t\t\t[3] Department Information
        \t\t\t\t\t[4] Student Information\n\t\t\t\t\t\t[5] Teacher Information
        \t\t\t\t\t[6] Course Information\n\t\t\t\t\t\t[7] Book Information
        \t\t\t\t\t[8] Result Information\n\n\t""")

        admin= input(Fore.CYAN+'\t\t\t\t\t\tEnter Your Choice: ')
        print(Fore.RESET)

        if admin=='1': addRegCourseInfo()
        elif admin=='2': addlibInfo()
        elif admin=='3': addDept()
        elif admin=='4': addStudent()
        elif admin=='5': addTeacher()
        elif admin=='6': addCourse()
        elif admin=='7': addBook()
        elif admin=='8': addResult()
        elif admin=='q': exit()



def addRegCourseInfo():
    
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t         ######  REGISTRATION INFORMATION  #######\n')
        print(Fore.RESET)

        while True:
            studentID = input("Enter Student ID (191-15-12381): ")
            c.execute("SELECT * FROM student WHERE studentID = ?",(studentID,))
            sInfo = c.fetchall()
            if len(sInfo)<1:
                print(f'Student ID {studentID} not found.')
                imenu = input("Continue or Press 'm' for menu: ")
            else: break
            if imenu == 'm': adminPanel()

        anotherCourse=''
        while anotherCourse != 'q':
            courseCode = input("Enter Course Code: ")
            semester = input("Enter semester (Summer-21): ")
            section = input("Enter Section: ")
            while True:
                teacherID = input("Enter Teacher ID: ")
                c.execute("SELECT * FROM teacher WHERE teacherID = ?",(teacherID,))
                tInfo = c.fetchall()
                if len(tInfo)<1:
                    print(f'Teacher ID {teacherID} not found.')
                    imenuT = input("Continue or Press 'm' for menu: ")
                else: break
                if imenuT == 'm': adminPanel()
        
            c.execute("INSERT INTO registeredCourse VALUES(?,?,?,?,?)",(studentID,courseCode,semester,section,teacherID,))

            print(f'\n\tRegistration Information of Student {studentID} and Course Code: {courseCode} Succesfully recorded.')
            anotherCourse = input("Want to add more courses? Press 'y' or 'q' for quit: ")

        another = input("Want to add another Student Registration Information? Press 'y' or 'q' for menu: ")
    conn.commit()



def addResult():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t         ######  RESULT INFORMATION  #######\n')
        print(Fore.RESET)

        while True:
            studentID = input("Enter Student ID (191-15-12381): ")
            c.execute("SELECT * FROM student WHERE studentID = ?",(studentID,))
            sInfo = c.fetchall()
            if len(sInfo)<1:
                print(f'Student ID {studentID} not found.')
                imenu = input("Continue or Press 'm' for menu: ")
            else: break
            if imenu == 'm': adminPanel()

        anotherCourse=''
        while anotherCourse != 'q':
            courseCode = input("Enter Course Code: ")
            c.execute("SELECT * FROM registeredCourse WHERE studentID =? AND courseCode = ?",(studentID,courseCode,))
            cInfo = c.fetchall()
            if len(cInfo)<1: 
                print(f'\n\tCourse {courseCode} not Registered.')
                input("Press any key to Try Again . . .")
                continue
            semester = input("Enter semester (Summer-21): ")
            grade = float(input("Enter Grade Point (3.25): "))
            
        
            c.execute("INSERT INTO result VALUES(?,?,?,?)",(studentID,courseCode,semester,grade,))

            print(f'\n\tResult of Student {studentID} and Course Code: {courseCode} Succesfully recorded.')
            anotherCourse = input("Want to add more courses? Press 'y' or 'q' for quit: ")

        another = input("Want to add another Student Result Information? Press 'y' or 'q' for menu: ")
    conn.commit()






def addlibInfo():
    
    another=''
    while another !='q':
        while True:
            screen_clear()
            print(Fore.CYAN+"""
        \t\t\t     _                 _                _        ____       _       _   
        \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
        \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
        \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
        \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
            print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
            print('\n\t\t\t\t         ########  LIBRARY INFORMATION  #########\n')
            print(Fore.RESET)
            studentID = input("Enter Student ID (191-15-12381): ")
            c.execute("SELECT * FROM student WHERE studentID = ?",(studentID,))
            sInfo = c.fetchall()
            if len(sInfo)<1:
                print(f'Student ID {studentID} not found.')
                imenu = input("Continue or Press 'm' for menu: ")
            else: break
            if imenu == 'm': adminPanel()

        bID = None
        Taken = None
        Return = None
        n = input("Taken any book? Press y/N: ")
        if n == 'y' or n =='Y':
            bID = input("Enter Book ID: ")
            c.execute("SELECT * FROM book WHERE bookID = ?",(bID,))
            bInfo = c.fetchall()
            if len(bInfo)>=1:
                Taken = input("Book is Taken (YYYY-MM-DD): ")
                Return = input("Book is Return (YYYY-MM-DD): ")
            else:
                print(f'Book ID {bID} not found. Try Again!')

            if Return == "": Return = None
        
        if len(bInfo)>=1:
            c.execute("INSERT INTO library VALUES(?,?,?,?)",(studentID,bID,Taken,Return,))
            print(f'\n\tLibrary Information of Student {studentID} Succesfully recorded.')

        another = input("Want to add another Student Library Information press 'y' or 'q' for menu: ")
    conn.commit()




def addDept():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t         #######  STUDENT INFORMATION  ########\n')
        print(Fore.RESET)
    
        dName =input("\tEnter Department Name: ")
        c.execute("SELECT * FROM department WHERE dName=?",(dName,))
        dInfo=c.fetchall()
        if len(dInfo)>=1: print(f'\n\t{dName} Department already exists.')
        else:
            c.execute("INSERT INTO department (dName) VALUES(?)",(dName,))
            print(f'\n\t{dName} Department successfully added.\n\n')

        another = input("Want to add another Student press 'y' or 'q' for menu: ")
    conn.commit()



def addStudent():
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t         #######  STUDENT INFORMATION  ########\n')
        print(Fore.RESET)
        print('\t\t\t\t[1] Edit Student Information\t[2] Add Student Information\n\n')
        choice = input("Enter your choice or 'q' for menu: ")
        if choice == '1' or choice =='2':
            sID = input("Enter Student ID: ")
        else: break
        c.execute("SELECT * FROM student WHERE studentID = ?",(sID,))
        sInfo = c.fetchall()
        if len(sInfo)>=1 and choice=='2': 
            print(f'\n\tTeacher {sID} already exists.')
        elif len(sInfo)<1 and choice == '1':
            print(f'Teacher ID {sID} not found.')
        elif len(sInfo) >=1 and choice =='1':
            studentID = input("Enter Student ID (191-15-12381): ")
            email = input("Enter Student Email: ")
            name = input("Enter Student Name: ")
            father = input("Enter Father Name: ")
            mother = input("Enter Mother Name: ")
            address = input("Enter Address: ")
            cell = input("Enter Student Cell Number: ")
            deptID = input("Enter Department ID: ")
            batch = input("Enter Student Batch: ")

            c.execute("UPDATE student SET studentID = ?, email = ?, name=?, fatherName = ?, motherName =?, address = ?, cell = ?, deptID = ?, batch =? WHERE studentID = sID",(studentID,email,name,father,mother,address,cell,deptID,batch,))
            print(f'\n\tStudent {studentID} Updated Succesfully.')

        else:
            studentID = input("Enter Student ID (191-15-12381): ")
            email = input("Enter Student Email: ")
            name = input("Enter Student Name: ")
            gender = input("Enter Student Gender: ")
            father = input("Enter Father Name: ")
            mother = input("Enter Mother Name: ")
            address = input("Enter Address: ")
            cell = input("Enter Student Cell Number: ")
            deptID = input("Enter Department ID: ")
            batch = input("Enter Student Batch: ")

            c.execute("INSERT INTO student VALUES(?,?,?,?,?,?,?,?,?,?)",(studentID,email,name,gender,father,mother,address,cell,deptID,batch,))
            print(f'\n\tStudent {studentID} Succesfully added.')
        another = input("Want to Add or Edit another Student press 'y' or 'q' for menu: ")
    conn.commit()
        


def addTeacher():
    
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t          #######  TEACHER INFORMATION  ########\n')
        print(Fore.RESET)
        print('\t\t\t\t[1] Edit Teacher Information\t[2] Add Teacher Information\n\n')
        choice = input("Enter your choice or 'q' for menu: ")
        if choice == '1' or choice =='2':
            tID = input("Enter Teacher ID or Employee ID: ")
        else: break
        c.execute("SELECT * FROM teacher WHERE teacherID = ?",(tID,))
        tInfo = c.fetchall()
        if len(tInfo)>=1 and choice=='2': 
            print(f'\n\tTeacher {tID} already exists.')
        elif len(tInfo)<1 and choice == '1':
            print(f'Teacher ID {tID} not found.')
        elif len(tInfo) >=1 and choice =='1':
            temail = input("Enter New Teacher Email: ")
            designation = input("Enter New Teacher Designation: ")
            cell = input("Enter New Mobile Number: ")
            c.execute("UPDATE teacher SET tEmail = ?, designation = ?, cell = ? WHERE teacherID = tID",(temail,designation,cell,))
            conn.commit()

        else: 
            temail = input("Enter Teacher Email: ")
            tname = input("Enter Teacher Name: ")
            tInitial = input("Enter Teacher Initial: ")
            designation = input("Enter Teacher Designation: ")
            deptID = input("Enter Department ID: ")
            cell = input("Enter Mobile Number: ")
            c.execute("INSERT INTO teacher VALUES(?,?,?,?,?,?,?)",(tID,temail,tname,tInitial,designation,deptID,cell))
            print(f'\n\tTeacher {tID} Succesfully added.')

        another = input("Want to Add or Edit another Teacher or Try Again press 'y' or 'q' for menu: ")
    conn.commit()



def addCourse():
    
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t          #######  COURSE INFORMATION  ########\n')
        print(Fore.RESET)
        courseCode = input("Enter Course Code (CSE312): ")
        courseTitle = input("Enter Course Title: ")
        courseCredit = float(input("Enter Course Credit: "))

        c.execute("SELECT * FROM course WHERE courseCode = ?",(courseCode,))
        cInfo = c.fetchall()
        if len(cInfo)>=1: print(f'\n\tCourse {courseCode} already exists.')
        else: 
            c.execute("INSERT INTO course VALUES(?,?,?)",(courseCode,courseTitle,courseCredit))
            print(f'\n\tCourse {courseCode} Succesfully added.\n\n')
        another = input("Want to add another Course press 'y' or 'q' for menu: ")
    conn.commit()


def addBook():
    
    another=''
    while another !='q':
        screen_clear()
        print(Fore.CYAN+"""
    \t\t\t     _                 _                _        ____       _       _   
    \t\t\t    / \   ___ __ _  __| | ___ _ __ ___ (_) ___  |  _ \ ___ (_)_ __ | |_ 
    \t\t\t   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __| | |_) / _ \| | '_ \| __|
    \t\t\t  / ___ \ (_| (_| | (_| |  __/ | | | | | | (__  |  __/ (_) | | | | | |_ 
    \t\t\t /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___| |_|   \___/|_|_| |_|\__|""")
        print('\n\t\t\t\t------ Welcome to the Palace of Student and Teacher -------')
        print('\n\t\t\t\t          #########  BOOK INFORMATION  ##########\n')
        print(Fore.RESET)
        bID = input("Enter Book ID: ")
        bName = input("Enter Book Name: ")
        bCategory = input("Enter Book Category: ")

        c.execute("SELECT * FROM book WHERE bookID = ?",(bID,))
        bInfo = c.fetchall()
        if len(bInfo)>=1: print(f'\n\tBook {bID} already exists.')
        else: 
            c.execute("INSERT INTO book VALUES(?,?,?)",(bID,bName,bCategory,))
            print(f'\n\tBook {bID} Succesfully added.')
        another = input("Want to add another Book press 'y' or 'q' for menu: ")
    conn.commit()


login()
