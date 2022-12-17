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


def open_correct_sheet(sheet_name, field_name, input_question):
    """
    The open_correct_sheet function opens the relevant sheet and returns the 
    user input
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    str_values = [str(record[field_name]) for record in sheet_info]
    print(str_values)
    check = False
    while not check:
        user_input = input(input_question).strip()
        user_str = str(user_input)
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


def target_check(student, sheet_name, field_name):
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
    target_value = current_user['target']
    print('check')
    print(current_user)
    print('check')
    if target_value == '':
        check = False
        while not check:
            user_target_input = input('What is your target % for the ' 
                                      'end of the year '
                                      '(Enter a percentage)? \n   ').strip()
            current_user['target'] = user_target_input
            if not user_target_input.isdigit():
                print('insert a number')
                continue
            elif int(user_target_input) <= 0:
                print('Minimum target is 1% try again \n')
                continue
            elif int(user_target_input) > 100:
                print('Target cannot be larger than 100% try again \n')
                continue
            else:
                print('Updating target...\n')
                print(current_user)
                no_of_rows = len(sheet_info)
                print(no_of_rows)
                # We +2 to take into account header and index starting from 0
                user_pos = str_values.index(f'{student}') + 2 
                print(user_pos)
                correct_sheet.delete_rows(user_pos)
                update_student = list(current_user.values())
                print(update_student)
                # In here create the a lsit of values for the current user 
                # and append
                correct_sheet.append_row(update_student)
                print('Target updated! \n')
                print(f'You need to achieve at least {user_target_input}%'
                      'on each assessment')
                check = True
                break       

           
def assessment_check(user_input, sheet_name, field_name):
    """
    This function will ask user to input their score for a specific assessment 
    number
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    str_values = [str(record[field_name]) for record in sheet_info]
    print(str_values)
    for school in sheet_info:
        for value in school.values():
            if str(value) == user_input:
                current_user = school
                print(current_user)
                break
    check = False
    while not check:
        user_assessment_no_input = input('What assessment number '
                                         'is this? \n   ').strip()
        if not user_assessment_no_input.isdigit():
            print('Insert a number')
            continue
        elif int(
                user_assessment_no_input) > 6 or int(
                                                    user_assessment_no_input
                                                    ) < 1:
            print('Insert a number from 1 to 6')
            continue
        elif current_user[f'{user_assessment_no_input}'] != '':
            print('This assessment already has data inputted. '
                  'Please try again.')
            continue
        else:
            print('Thank you for a valid assessment number \n')
            
        user_assessment_before = int(user_assessment_no_input) - 1
        if user_assessment_before != 0:
            if current_user[f'{user_assessment_before}'] == '':
                print(f'There is not data for {user_assessment_before}, '
                      'are you sure this assessment number is correct? '
                      'Try again \n')
                continue
            else:
                check_two = False
                while not check_two:
                    user_score_input = input('What is your score '
                                             '(out of 100)? \n   ').strip()
                    if not user_score_input.isdigit():
                        print('Please insert a number \n')
                        continue
                    elif int(
                            user_score_input) > 100 or int(
                                                           user_score_input
                                                            ) < 0:
                        print('Please insert a valid score \n')
                    else:
                        current_user[
                            f'{user_assessment_no_input}'
                                    ] = user_score_input
                        print('Updating grade...\n')
                        no_of_rows = len(sheet_info)
                        print(no_of_rows)
                        user_pos = str_values.index(f'{user_input}') + 2 
                        # We +2 to take into account header and index starting 
                        # from 0
                        print(user_pos)
                        correct_sheet.delete_rows(user_pos)
                        update_student = list(current_user.values())
                        print(update_student)
                        correct_sheet.append_row(update_student)
                        print(current_user)
                        print('Grade updated! \n')
                        check_two = True
                        check = True
        else:
            # if user inputs 1, then no need to check any other data has been 
            # written previously
            check_two = False
            while not check_two:
                user_score_input = input('What is your score (out of 100)? \n')
                if not user_score_input.isdigit():
                    print('Please insert a number')
                    continue
                elif int(user_score_input) > 100 or int(user_score_input) < 0:
                    print('Please insert a valid score')
                else:
                    current_user[
                        f'{user_assessment_no_input}'
                                ] = user_score_input
                    print('Updating target...\n')
                    no_of_rows = len(sheet_info)
                    print(no_of_rows)
                    user_pos = str_values.index(f'{user_input}') + 2 
                    # We +2 to take into account header and index starting 
                    # from 0
                    print(user_pos)
                    correct_sheet.delete_rows(user_pos)
                    update_student = list(current_user.values())
                    print(update_student)
                    correct_sheet.append_row(update_student)
                    print(current_user)
                    print('Grade updated! \n')
                    check_two = True
                    check = True
    return user_assessment_no_input


def new_grade_aim(assessment_number, user_input, sheet_name, field_name):
    """
    The new_grade_aim function takes the users data from assessment 1 up to 6 
    and finds the average grade so far
    Then it calculates, how much you need for the next assessment to reach 
    target if the last assessment is not the sixth one.
    If it is, then just calculate the average.
    If the avergae is less than target, a message says try again next year!
    If it meets target, a message says well done for reaching target!
    If it exceeds target, a message says well done for exceed target!
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    str_values = [str(record[field_name]) for record in sheet_info]
    print(str_values)
    for school in sheet_info:
        for value in school.values():
            if str(value) == user_input:
                current_user = school
                print(current_user)
                break
    student_values_dict = current_user.values()
    student_values_list = list(student_values_dict)
    print(student_values_list)
    student_values_list.reverse()
    print(student_values_list)
    student_values = student_values_list[:6]
    print(student_values)
    num = 0
    for i in student_values:
        if i == '':
            continue
        else:
            num += i

    average = num/int(assessment_number)
    print(num)
    if assessment_number == '6':
        if average == current_user['target']:
            print('Well done, you\'ve acheived you\'re target')
        elif average > current_user['target']:
            print('You have exceed the target! Well done!')
        else: 
            print('You have not reached the target yet, '
                  'try again next year \n')
    else:
        if average == current_user['target']:
            print('Well done, you\'ve acheived you\'re target')
        elif average > current_user['target']:
            print('You have exceed the target! Keep it up')    
    print(average)
    print(current_user['target'])


def main():
    """
    Main function where
    """
    user_school_input = open_correct_sheet(
        'school_number', 'Number:', 'What is your School ID? \n')
    user_user_input = open_correct_sheet(
        user_school_input, 'user number', 'What is your User ID? \n')
    target_check(user_user_input, user_school_input, 'user number')
    check_assessment_info = assessment_check(
        user_user_input, user_school_input, 'user number')
    new_grade_aim(
        check_assessment_info, user_user_input, 
        user_school_input, 'user number')


main()
