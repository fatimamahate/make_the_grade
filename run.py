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
        for info in str_values:
            if info != user_input:
                print('This number is invalid, try again')
                break
            else: 
                for school in sheet_info:
                    for value in school.values():
                        if str(value) == user_input:
                            print(school)
                print('Thank you for the correct ID')
                check = True
                break
    return user_input

def assessment_check(student,sheet_name,field_name):
    """
    This takes school number and user number from above
    Checks if user has a target value and total number of assessments
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    for school in sheet_info:
        for value in school.values():
            if str(value) == student:
                print(school)
    last_key = list(school)[-1]
    if last_key == 'target':
        check = False
        while not check:
            user_target_input=input('What is your target % for the end of the year (Enter a percentage)? \n')
            if int(user_target_input) <= 0:
                print('Minimum target is 1% try again')
                continue
            elif int(user_target_input) > 100:
                print('Target cannot be larger than 100% try again')
                continue
            else:
                print('Updating target...\n')
                print(f'You need to achieve at least {last_key}% on each assessment')
                check = True
                break
    
    user_assessment_no_input= input('What is the assessment number?') 
    if user_assessment_no_input != int(last_key)+1:
        print(f'Are you sure? The last assessment number was {last_key}')              
    


user_school_input = open_correct_sheet('school_number', 'Number:', 'What is your School ID? \n')
user_user_input = open_correct_sheet(user_school_input, 'user number', 'What is your User ID? \n')
check_student_info = assessment_check(user_user_input, user_school_input, 'user number')


