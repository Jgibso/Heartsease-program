Num_vol = int(input('How many volunteers will use this program: '))

# Loop through each volunteer
for Voluteers in range(Num_vol):
    print('')
    name = input('Enter Volunteer name: ')
    print(name, 'ID Num', '(', Voluteers + 1, ')')
    print('------------------------------')

    # Collect answers for health symptoms
    Ans_one = input("Enter 'yes' or 'no' if you are lightheaded: ")
    Ans_two = input("Enter 'yes' or 'no' if you have irregular heartbeat: ")
    Ans_three = input("Enter 'yes' or 'no' if you have shortness of breath: ")
    Ans_four = input("Enter 'yes' or 'no' if you are more tired than usual: ")
    Ans_five = input("Enter 'yes' or 'no' if your feet or ankles are swollen: ")
    Ans_six = input("Enter 'yes' or 'no' if you have not been yourself: ")

    # Convert responses to booleans
    try:
        answer1 = Ans_one.lower() == 'yes'
        answer2 = Ans_two.lower() == 'yes'
        answer3 = Ans_three.lower() == 'yes'
        answer4 = Ans_four.lower() == 'yes'
        answer5 = Ans_five.lower() == 'yes'
        answer6 = Ans_six.lower() == 'yes'
    except ValueError:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue  # Skip this iteration if there is invalid input

    # Decision based on the boolean answers
    if answer1 and answer2 and answer3 and answer4 and answer5 and answer6:
        print("You have all the symptoms of heart disease, please contact a healthcare provider.")
    elif not any([answer1, answer2, answer3, answer4, answer5, answer6]):
        print("You have no symptoms of heart disease, but still make sure you go for regular check-ups.")
    else:
        print("You have some symptoms, it is advised to contact a healthcare professional.")