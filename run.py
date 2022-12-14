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





def school_data():
    """
    The school_data function checks if the School ID inputted by user is valid
    """
    
    schools = SHEET.worksheet('school_number')
    current_sheet=schools.get_all_records()
    check = False
    while not check:
        user_school_no = input('What is your School ID? \n').strip()
        for p in current_sheet:
            if str(p['Number:']) == user_school_no:
                current_school = SHEET.worksheet((f"{user_school_no}"))
                print(current_school)
                check = True
                return user_school_no
        print('Invalid school ID , try again or contact school admin \n')
    

def user_data(id):
    """
    The user_data function opens the correct school worksheet and asks user to input user ID.
    It will check if the user id is in the data
    """
    school_id = str(id)
    check = False
    while not check:
        user_user_no = input('What is your User ID? \n').strip()
        correct_school = SHEET.worksheet(f'{id}')
        current_sheet = correct_school.get_all_records()
        # if not isdigit(user_user_no):
        #     print('enter a valid number')
        #     continue
        for p in current_sheet:
            if str(p['user number']) == user_user_no:
                current_student = p
                print(current_student)
                check = True
                return user_user_no
        print('Invalid user ID , try again or contact school admin \n')

# # def assessment_check(student):
# #     """
# #     The input in this will be the return of the previous function (user_user_no) which is a list and will ask user to fill in 
# #     """
# #     if student

    

act_school= school_data()
student=user_data(act_school)


