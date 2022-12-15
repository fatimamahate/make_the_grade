import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CRED = Credentials.from_service_account_file('creds.json')
SCOPED_CRED = CRED.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CRED)
SHEET = GSPREAD_CLIENT.open('make_the_grade')


def open_correct_sheet(sheet_name,field_name,input_question):
    """
    The open_correct_sheet function opens the relevant sheet and returns the user input
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    str_values = [str(record[field_name]) for record in sheet_info]
    print(str_values)
    check = False
    while not check:
        user_input = input(input_question).strip()
        user_str=str(user_input)
        if user_str not in str_values:
            print('This number is invalid, try again')
        else: 
            for school in sheet_info:
                for value in school.values():
                    if str(value) == user_str:
                        print(school)
            print('Thank you for the correct ID')
            check = True
    return user_input

def assessment_check(student,sheet_name,field_name):
    """
    This takes school number and user number from above
    Checks if user has a target value and total number of assessments
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    str_values = [str(record[field_name]) for record in sheet_info]
    print(str_values)
    for school in sheet_info:
        for value in school.values():
            if str(value) == student:
                current_user = school
                print(current_user)
                break
    last_key = list(school)[-1]
    print('check')
    print(current_user)
    print('check')
    if last_key == 'target':
        check = False
        while not check:
            user_target_input=input('What is your target % for the end of the year (Enter a percentage)? \n')
            current_user['target'] = user_target_input
            if not user_target_input.isdigit():
                print('insert a number')
            elif int(user_target_input) <= 0:
                print('Minimum target is 1% try again')
                continue
            elif int(user_target_input) > 100:
                print('Target cannot be larger than 100% try again')
                continue
            else:
                print('Updating target...\n')
                print(current_user)
                no_of_rows = len(sheet_info)
                print(no_of_rows)
                user_pos=str_values.index(f'{student}') + 2 #We +2 to take into account header and index starting from 0
                print(user_pos)
                temp_delete = correct_sheet.delete_rows(user_pos)
                update_student = list(current_user.values())
                print(update_student)
                ##In here create the a lsit of values for the current user and append
                correct_sheet.append_row(update_student)
                print('Target updated! \n')
                print(f'You need to achieve at least {user_target_input}% on each assessment')
                check = True
                break
    
    # user_assessment_no_input= input('What is the assessment number?') 
    # if user_assessment_no_input != int(#assessment number)+1:
    #     print(f'Are you sure? The last assessment number was {last_key}')              
    
"""
TO-DO
add user assessment func

"""
user_school_input = open_correct_sheet('school_number', 'Number:', 'What is your School ID? \n')
user_user_input = open_correct_sheet(user_school_input, 'user number', 'What is your User ID? \n')
check_student_info = assessment_check(user_user_input, user_school_input, 'user number')


