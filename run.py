"""
Make The Grade can allow for students to input their assessment score
to aid school work.
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
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
    check = False
    while not check:
        user_input = input(input_question).strip()
        user_str = str(user_input)
        if user_str not in str_values:
            print('This number is invalid, try again \n')
        else:
            for school in sheet_info:
                for value in school.values():
                    if str(value) == user_str:
                        print('Thank you for the correct ID \n')
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
    for user in sheet_info:
        for value in user.values():
            if str(value) == student:
                current_user = user
                break
    target_value = current_user['target']
    if target_value == '':
        check = False
        while not check:
            user_target_input = input('What is your target % for the '
                                      'end of the year (Whole number '
                                      'out of 100)? \n   ').strip()
            current_user['target'] = user_target_input
            if not user_target_input.isdigit():
                print('Please insert a valid, whole number \n')
                continue
            elif int(user_target_input) <= 0:
                print('The minimum target is 1%, try again \n')
                continue
            elif int(user_target_input) > 100:
                print('The Target cannot be larger than 100%, try again \n')
                continue
            else:
                print('Updating target...\n')
                # We +2 to take into account header and index starting from 0
                user_pos = str_values.index(f'{student}') + 2
                correct_sheet.delete_rows(user_pos)
                update_student = list(current_user.values())
                # In here create the a lsit of values for the current user
                # and append
                correct_sheet.append_row(update_student)
                print('Target updated! \n')
                print(f'You need to achieve at least {user_target_input}%'
                      ' on each assessment \n')
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
    for user in sheet_info:
        for value in user.values():
            if str(value) == user_input:
                current_user = user
                break
    check = False
    while not check:
        data_input = input('\n Are you adding a score? (Press 1 for yes and 0 '
                           'for no) \n Please note that you cannot add a '
                           'score once all 6 assessments have been '
                           'completed.\n   ')
        if data_input == '1':
            user_assessment_input = input('What assessment number is this?'
                                          ' (Assessment 1 to 6) '
                                          '\n   ').strip()
            if not user_assessment_input.isdigit():
                print('Insert a valid, whole number \n')
                continue
            elif int(
                    user_assessment_input
                                            ) > 6 or int(
                                                        user_assessment_input
                                                        ) < 1:
                print('Insert a number from 1 to 6 \n')
                continue
            elif current_user[f'{user_assessment_input}'] != '':
                print('This assessment already has data inputted. '
                      'Please try again. \n')
                continue
            else:
                print('Thank you for a valid assessment number \n    ')
            user_assessment_before = int(user_assessment_input) - 1
            if user_assessment_before != 0:
                if current_user[f'{user_assessment_before}'] == '':
                    print(f'There is no data for {user_assessment_before}, '
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
                                f'{user_assessment_input}'
                                        ] = user_score_input
                            print('Updating score...\n')
                            user_pos = str_values.index(f'{user_input}') + 2
                            # We +2 to take into account header and index
                            # from 0
                            correct_sheet.delete_rows(user_pos)
                            update_student = list(current_user.values())
                            correct_sheet.append_row(update_student)
                            print('Score updated! \n')
                            check_two = True
                            check = True
            else:
                # if user inputs 1, then no need to check any other data was
                # written previously
                check_two = False
                while not check_two:
                    user_score_input = input('What is your score '
                                             '(out of 100)? \n   ')
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
                            f'{user_assessment_input}'
                                    ] = user_score_input
                        print('Updating score...\n')
                        user_pos = str_values.index(f'{user_input}') + 2
                        # We +2 to take into account header and index starting
                        # from 0
                        correct_sheet.delete_rows(user_pos)
                        update_student = list(current_user.values())
                        correct_sheet.append_row(update_student)
                        print('Score updated! \n')
                        check_two = True
                        check = True
                        return user_assessment_input
        elif data_input == '0':
            check = True
        else:
            print('Please enter either 1 for yes or 0 for no')
    return user_assessment_input


def new_grade_aim(assessment_number, user_input, sheet_name):
    """
    The new_grade_aim function takes the users data from assessment 1 up to 6
    and finds the average grade
    """
    if assessment_number is None:
        return
    else:
        correct_sheet = SHEET.worksheet(sheet_name)
        sheet_info = correct_sheet.get_all_records()
        for user in sheet_info:
            for value in user.values():
                if str(value) == user_input:
                    current_user = user
        student_values_dict = current_user.values()
        student_values_list = list(student_values_dict)
        student_values_list.reverse()
        student_values = student_values_list[:6]
        num = 0
        for i in student_values:
            if i == '':
                continue
            else:
                num += i

        average = num/int(assessment_number)
        if assessment_number == '6':
            if average == current_user['target']:
                print('Well done, you\'ve acheived you\'re target \n')
            elif average > current_user['target']:
                print('You have exceed the target! Well done! \n')
            else:
                print('You have not reached the target yet, '
                      'try again next year \n')


def data_check(user_input, sheet_name):
    """
    This function prints the data we currently have for user
    """
    correct_sheet = SHEET.worksheet(sheet_name)
    sheet_info = correct_sheet.get_all_records()
    for user in sheet_info:
        for value in user.values():
            if str(value) == user_input:
                current_user = user
                name = current_user['name']
                print(f'The data we currently have for {name} is ...')
                print(current_user)
                break
    if current_user['6'] != '':
        print('Thank you for using Make The Grade.')
        return


def main():
    """
    Main function where everything is run
    """
    print('Welcome to Make The Grade!!')
    user_school_input = open_correct_sheet(
        'school_number', 'Number:', 'What is your School ID? \n   ')
    user_user_input = open_correct_sheet(
        user_school_input, 'user number', 'What is your User ID? \n   ')
    target_check(user_user_input, user_school_input, 'user number')
    data_check(user_user_input, user_school_input)
    check_assessment_info = assessment_check(
        user_user_input, user_school_input, 'user number')
    data_check(user_user_input, user_school_input)
    new_grade_aim(
        check_assessment_info, user_user_input,
        user_school_input)


main()
