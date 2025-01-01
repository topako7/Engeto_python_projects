import re # re module is used for cleaning the text with regular expressions 


# ----- FUNCTIONS ---------------------------------------------------------------------------------------------------------

def clean_text(num):
    """
    Cleans the text selected by the user, removing non-alphanumeric characters.
    :param num: Index of the selected text (1, 2, or 3).
    :return: Cleaned text.
    """

    TEXTS = ['''
        Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley. ''',
        '''At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.''',
        '''The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie some
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as paddlefish,
        garpike and stingray are also present.'''
     ]
    
        # to clean the text from extra spaces, dots, commas, etc.
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', TEXTS[num-1])
    #print(cleaned_text)
    
    return cleaned_text


def valid_number_input():
    """
    Prompts the user to input a valid number (1, 2, or 3).
    If the input is invalid, it will continue prompting until a valid number is entered.
    :return: Valid number selected by the user (1, 2, or 3).
    """

    while True:
        try:
                # Prompt the user for input
            user_input = input("Enter a number btw. 1 and 3 to select: ")
            
                # Try to convert the input to an integer
            number = int(user_input)
            
                # Check if the number is within the valid range
            if number in (1, 2, 3):
                #print(f"Valid number entered: {number}")
                return number  # Exit the loop and return the valid number
            else:
                print("Invalid number! Please enter 1, 2, or 3.")
        except ValueError:
            # Handle the case where the input is not a number
            print("Input is not a valid number. Please try again.")


def text_analyze(text: str):
    """
    Analyzes the given text by counting different word categories such as titlecase, uppercase, lowercase, and numeric words.
    It also prints a summary of word length frequencies and numeric sum.
    :param text: The cleaned text for analysis.
    
    Example of output:
    There are 54 words in the selected text.
    There are 12 titlecase words.
    There are 1 uppercase words.
    There are 38 lowercase words.
    There are 3 numeric strings.
    The sum of all numbers 8510
    ----------------------------------------
    LEN|  OCCURENCES  |NR.
    ----------------------------------------
    1  |*             |1
    2  |*********     |9
    3  |******        |6
    4  |***********   |11
    5  |************  |12
    6  |***           |3
    7  |****          |4
    8  |*****         |5
    9  |*             |1  
    10 |*             |1
    11 |*             |1

    """
  
        # setup the variables
    words = text.split()
    titlecase_word = 0
    uppercase_word = 0
    lowercase_word = 0
    num_count = 0
    num_sum = 0
    longest_word = 0
    word_count = dict()

        # loop that passes through the cleaned words from the given text
    for word in words:
            # count words with the same lenght.
        word_count[len(word)] = word_count.get(len(word), 0) + 1

            # save the lenght of longest word in the text (to define the output table that will be printed)
        longest_word = max(longest_word, len(word)) 

            # count words with the first upper case letter and also is not a numeric or special character 
        if word[0].isupper() and word[0].isalpha(): 
            titlecase_word += 1
            # print(f"titlecase word: {word}")

            # count of the words with all upper case letters and the whole word does not contain a number or special character
        if word.isupper() and word.isalpha(): 
            uppercase_word += 1
            # print(f"uppercase word: {word}")
            
            # count of the words with all lower case letters and the whole word does not contain a number or special character
        if word.islower() and word.isalpha(): 
            lowercase_word += 1
            # print(f"lowercase word: {word}")

            # count of the words that are numbers 
        if word.isnumeric(): 
            num_count += 1
            num_sum += int(word)


        # Determine the maximum frequency for word lengths
    max_length = max(word_count.values(), default=12)
    max_length = max(max_length, 12)  # Ensure the minimum length is 12
    
        # print the analysis results
    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {titlecase_word} titlecase words.")
    print(f"There are {uppercase_word} uppercase words.")
    print(f"There are {lowercase_word} lowercase words.")
    print(f"There are {num_count} numeric strings.")
    print(f"The sum of all numbers {num_sum}")
    print(f"----------------------------------------")
    print(f"{'LEN|':<4} {'OCCURENCES':^{max_length}} {'|NR.':<4}")
    print(f"----------------------------------------")
    
        # this loop ensure the printing of layout for each lenght of words within the text
    for i in range(1, longest_word + 1):
        n = word_count.get(i, 0)
        print(f"{i:<3}|{'*' * n:<{max_length+2}}|{n:<3}")
    

def check_user(username, password) -> bool:
    """
    Verifies if the given username and password match the stored credentials.
    :param username: The username input by the user.
    :param password: The password input by the user.
    :return: True if the username and password match, otherwise False.
    """
        # Ensure inputs are strings
    username = str(username)
    password = str(password)
    
        # Defined data of users - should be check by unique test if this will be dynamic.
    data = {
        "bob"   :"123",
        "ann"   :"pass123",
        "mike"  :"password123",
        "liz"   :"pass123" 
    }

        # Check if the username exists and if the password matches
    return data.get(username) == password


# ----- MAIN ----------------------------------------------------------------------------------------------------------------

    # inputs from user to check the credentials
username = input("Enter your username: ")
password = input("Enter your password: ")
result = check_user(username, password)

    # output the results from user verification
if result: 
    print(f"----------------------------------------")
    print(f"Welcome to the app, {username}.")
    print(f"We have 3 texts to be analyzed.")
    print(f"----------------------------------------")
    text_num = valid_number_input()
    print(f"----------------------------------------")
    text_analyze(clean_text(text_num))
else: 
    print(f"unregistered user, terminating the program..")
