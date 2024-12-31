def texts(num):

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
    return TEXTS[num-1]

def valid_number_input():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Enter a number btw. 1 and 3 to select: ")
            
            # Try to convert the input to an integer
            number = int(user_input)
            
            # Check if the number is within the valid range
            if number in (1, 2, 3):
                print(f"Valid number entered: {number}")
                return number  # Exit the loop and return the valid number
            else:
                print("Invalid number! Please enter 1, 2, or 3.")
        except ValueError:
            # Handle the case where the input is not a number
            print("Input is not a valid number. Please try again.")


def text_analyze(text: str):
    
    cleaned_text = text.replace(",", "").replace(".", "").strip()
    words = cleaned_text.split()
    print(cleaned_text)

    print(f"There are {len(words)} words in the selected text.")
    
    titlecase_word = 0
    uppercase_word = 0
    lowercase_word = 0
    num_count = 0
    num_sum = 0
    for word in words:
        if word[0].isupper() and word[0].isalpha(): 
            titlecase_word += 1
            # print(f"titlecase word: {word}")
        if word.isupper() and word[0].isalpha(): 
            uppercase_word += 1
            # print(f"uppercase word: {word}")
        if word.islower(): 
            lowercase_word += 1
            # print(f"lowercase word: {word}")
        if word.isnumeric(): 
            num_count += 1
            num_sum += int(word)

    print(f"There are {titlecase_word} titlecase words.")
    print(f"There are {uppercase_word} uppercase words.")
    print(f"There are {lowercase_word} lowercase words.")
    print(f"There are {num_count} numeric strings.")
    print(f"The sum of all numbers {num_sum}")



def check_user(username, password) -> bool:
    """
    Verifies if the given username and password match the stored credentials.
    """
    # Ensure inputs are strings
    username = str(username)
    password = str(password)
    
    # Defined data of users - this should be check by unique test if it will be dynamic
    data = {
        "bob"   :"123",
        "ann"   :"pass123",
        "mike"  :"password123",
        "liz"   :"pass123" 
    }

    if username in data: 
        return data[username] == password
    return False

username = input("Enter your username: ")
password = input("Enter your password: ")

result = check_user(username,password)

if result: 
    print(f"----------------------------------------")
    print(f"Welcome to the app, {username}.")
    print(f"We have 3 texts to be analyzed.")
    print(f"----------------------------------------")
    text_num = valid_number_input()
    print(f"----------------------------------------")
    text_analyze(texts(text_num))


else: print(f"unregistered user, terminating the program..")
