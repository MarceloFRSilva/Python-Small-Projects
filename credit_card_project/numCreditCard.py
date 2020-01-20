import random

#This represents the table used to verify the 
#validity of a certain card number
#The used algorithm to verify the card is the 
#Luhn algorithm
network = ["American Express", "Diners Club International", 
        "Discover Card", "Maestro", "Master Card", "Visa Electron", "Visa"]

abbreviations = ["AE", "DCI", "DC", "M", "MC", "VE", "V"]

initial_digits = [(34, 37), (309, 36, 38, 39), 65, 
                (5018, 5020, 5038), (50, 51, 52, 53, 54, 19),
                (4026, 426, 4405, 4508), (4024, 4532, 4556)]

number_of_digits = [15, 14, 16, (13, 19), 16, 16, (13, 16)]

################
#              #
#  Main Code   #
#              #
################

'''
    This function verifies is a certain card
    number is valid or not.
    As input it receives a number that corresponds
    to the credit card id.
    If a certain credit card number is correct 
    the card network as well as the entity category
    that emited the card (based on the table above).
    @return tuple containing the category and credit
    card network if it is a valid card number and 
    the character array 'invalid card' otherwise.
'''
def verify_cc(card_Id):
    if(luhn_algorithm(card_Id)):
        if(getNetworkEntity(card_Id)):
            return True
    print("Wrong card ID")        
    return False

'''
    This function generates a random card number based
    on the above table (represented by lists)
    As input it receives a char arry that corresponds
    to the abbreviations of the entities.
    @args abbreviations -> char array
    @return card_Id -> int
'''
def generate_cc_number(abbreviation):
    index = searchAbbreviation(abbreviation)
    card_Id = 0
    if(index > 0):
        incomplete_card_Id = generateInitialDigits(index)
        card_Id = generateTheRestOfTheCardId(incomplete_card_Id, index)
    return card_Id

#########################
#                       #
#  Auxiliar functions   #
#                       #
#########################

'''
    This function executes the Luhn algorithm
    It recevies a card_Id and verifies if it is valid or not
    @args card_Id -> integer
    @return boolean
'''
def luhn_algorithm(card_Id):
    if(card_Id == 0):
        return False
    last_digit = card_Id%10
    remove_last_digit = card_Id//10
    inverted_number = invert_number(remove_last_digit)
    duplicated_odd_number = duplicate_odd_position_number(inverted_number)
    add_digits_of_number = add_all_digits_of_a_number(duplicated_odd_number, last_digit)
    if(add_digits_of_number%10 == 0):
        return True
    return False

'''
    This function reveives a number and inverts it.
    @args number -> integer
    @return inverted_number -> integer
'''
def invert_number(number):
    inverted_number = 0
    while(number != 0):
        num1 = number % 10
        inverted_number = inverted_number*10 + num1
        number = number//10
    return inverted_number

'''
    This function reveives a number and duplicates
    the digits in the odd number positions, example
    1234 -> 2264 in which 1 and 3 got duplicated.
    @args number -> integer
    @return duplicated_odd_number -> integer
'''
def duplicate_odd_position_number(number):
    duplicated_odd_number = 0
    num_list = list(str(number))
    length = len(num_list)
    for i in range(0, length):
        if(i%2==0):
            if((int(num_list[i]) * 2) > 9):
                duplicated_odd_number = duplicated_odd_number * 10 + ((int(num_list[i]) * 2) - 9)
            else:
                duplicated_odd_number = duplicated_odd_number * 10 + int(num_list[i]) * 2
        else:
            duplicated_odd_number = duplicated_odd_number * 10 + int(num_list[i])
    return duplicated_odd_number

'''
    This function reveives a number and adds
    the digits in that number, example
    1234 -> 10 in which 1+2+3+4 = 10
    @args number -> integer
    @return add_digits_of_number -> integer
'''
def add_all_digits_of_a_number(number, last_digit):
    add_digits_of_number = 0
    while(number != 0):
        add_digits_of_number = add_digits_of_number + number%10
        number = number//10
    return add_digits_of_number + last_digit

'''
    This function reveives a credit card number and 
    returns the Network and respective category
    @args number -> integer
    @return network_and_category -> string
'''
def getNetworkEntity(card_Id):
    length = len(number_of_digits)
    for i in range(0, length):
        try:
            value = int(number_of_digits[i])
            if(number_of_digits[i] == len(str(card_Id))):
                if(verifyInitialValues(i, card_Id)):
                    return True
        except TypeError:
            for j in number_of_digits[i]:
                if(j == len(str(card_Id))):
                    if(verifyInitialValues(i, card_Id)):
                        return True
            continue
    return False

'''
    This function reveives an index and a card id and 
    returns a boolean verifying if the initial values are correct
    @args index and number -> integers
    @return boolean
'''
def verifyInitialValues(index, card_Id):
    try:
        value = int(initial_digits[index])
        sizeof_initial_value = int(len(str(initial_digits[index])))
        if(initial_digits[index] == int(str(card_Id)[:sizeof_initial_value])):
            print("The card belongs to the network: " + network[index])
            return True
    except TypeError:
        length = len(initial_digits[index])
        for j in range(0, length):
            sizeof_initial_value = int(len(str(initial_digits[index][j])))
            if(initial_digits[index][j] == int(str(card_Id)[:sizeof_initial_value])):
                print("The card belongs to the network: " + network[index])
                return True
    return False

'''
    This function reveives an abbreviation and  
    returns the corresponding index based on the abbreviations list
    @args abbreviation -> char array
    @return positive integer if the abbreviation exists -1 otherwise
'''
def searchAbbreviation(abbreviation):
    length = len(abbreviations)
    for i in range(0, length):
        if(abbreviations[i] == abbreviation):
            return i
    return -1

'''
    This function reveives an index and  
    returns the initial values using the list initial_digits above
    @args index -> integer
    @return initial_value -> integer 
'''
def generateInitialDigits(index):
    initial_value = 0
    try:
        value = int(initial_digits[index])
        initial_value = initial_digits[index]
    except TypeError:
        random_index = random.randint(0, len(initial_digits[index]) - 1)
        initial_value = initial_digits[index][random_index]
    
    return initial_value

'''
    This function reveives an incomplete card_Id with only 
    the initial values and an index then it
    returns the final card_Id completed with random values 
    using the list number_of_digits above
    @args incomplete_card_Id -> integer
    @return card_Id -> integer 
'''
def generateTheRestOfTheCardId(incomplete_card_Id, index):
    card_Id = 0
    current_num_size = len(str(incomplete_card_Id))
    num_missing_digits = 0
    while(not luhn_algorithm(card_Id)):
        card_Id = incomplete_card_Id
        try:
            value = int(number_of_digits[index])
            num_missing_digits = number_of_digits[index] - current_num_size
        except TypeError:
            random_index = random.randint(0, len(number_of_digits[index]) - 1)
            num_missing_digits = number_of_digits[index][random_index] - current_num_size
        if(num_missing_digits != 0):
            for i in range(0, num_missing_digits):
                random_value = random.randint(0, 9)
                card_Id = card_Id * 10 + random_value
    return card_Id

######################
#                    #
#  Test Operations   #
#                    #
######################
#print(invert_number(12345))
#print(duplicate_odd_position_number(1234567))
#print(add_all_digits_of_a_number(1234, 5))
#print(verify_cc(4556737586899855))
#verify_cc(4556737586899855) # Visa card
#verify_cc(375673758689856) # American Express
#verify_cc(30967375868969) # Diners Club International
#verify_cc(6556737586899850) # Discover Card
#verify_cc(5038737586896) # Maestro
#verify_cc(5018737586899855121) # Maestro
#verify_cc(5056737586899857) # Master Card
#verify_cc(4026737586899857) # Visa Electron
#verify_cc(4024737586899859) # Visa
#verify_cc(6554615813812884) # Wrong
#print(searchAbbreviation("VE"))
#print(generateInitialDigits(searchAbbreviation("VE")))
#print(generateTheRestOfTheCardId(52, 4))

#Final funtions test
generated_cc = generate_cc_number('MC')
print(generated_cc)
verify_cc(generated_cc)
generated_cc = generate_cc_number('DC')
print(generated_cc)
verify_cc(generated_cc)
generated_cc = generate_cc_number('V')
print(generated_cc)
verify_cc(generated_cc)
generated_cc = generate_cc_number('VE')
print(generated_cc)
verify_cc(generated_cc)

