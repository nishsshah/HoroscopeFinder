import requests
from bs4 import BeautifulSoup


'''
    "1. print greeting message on screen, asking for user's name
    "2. ask user for birthdate in format: mm/dd
    "3. extract month and day from input -> function (input = mm/dd and output = month and day)
    "4. given month and day, compute zodiac sign --> function (input = month and day and output = zodiac) (conditionals)
    "5. given zodiac obtain horoscope --> function (connect to url and return horoscope)
'''


def get_monthday(birthday):
    
    """
    Produces the month and day out of input date.

    Parameters
    ----------
    birthday : string
        Date formatted mm/dd

    Returns
    -------
    list or None
        Returns the month and day as a list. Returns None if the input format or values are incorrect.
    """
        
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(birthday) !=5 or birthday[2] != '/' or birthday[0] not in numbers:
        return None
    month = int(birthday[:2])
    day = int(birthday[3:])
    if month < 1 or month > 12 or day < 1 or day > 31:
        return None
    if month == 2 and day > 29:
        return None
    return [month, day]





def get_zodiac(my_lst):
    
    """
    Produces the zodiac sign based on the month and day given.

    Parameters
    ----------
    my_lst : list
        List containing the month and day.

    Returns
    -------
    str
        zodiac sign
    """
    if type(my_lst) != list:
        return None
        
    if (my_lst[0] == 12 and my_lst[1] >= 22) or (my_lst[0] == 1 and my_lst[1] <= 19):
        output = 'capricorn'
    elif (my_lst[0] == 1 and my_lst[1] >= 20) or (my_lst[0] == 2 and my_lst[1] <= 18):
        output = 'aquarius'
    elif (my_lst[0] == 2 and my_lst[1] >= 19) or (my_lst[0] == 3 and my_lst[1] <= 20):
        output = 'pisces'
    elif (my_lst[0] == 3 and my_lst[1] >= 21) or (my_lst[0] == 4 and my_lst[1] <= 19):
        output = 'aries'
    elif (my_lst[0] == 4 and my_lst[1] >= 20) or (my_lst[0] == 5 and my_lst[1] <= 20):
        output = 'taurus'
    elif (my_lst[0] == 5 and my_lst[1] >= 21) or (my_lst[0] == 6 and my_lst[1] <= 20):
        output = 'gemini'
    elif (my_lst[0] == 6 and my_lst[1] >= 21) or (my_lst[0] == 7 and my_lst[1] <= 22):
        output = 'cancer'
    elif (my_lst[0] == 7 and my_lst[1] >= 23) or (my_lst[0] == 8 and my_lst[1] <= 22):
        output = 'leo'
    elif (my_lst[0] == 8 and my_lst[1] >= 23) or (my_lst[0] == 9 and my_lst[1] <= 22):
        output = 'virgo'
    elif (my_lst[0] == 9 and my_lst[1] >= 23) or (my_lst[0] == 10 and my_lst[1] <= 22):
        output = 'libra'
    elif (my_lst[0] == 10 and my_lst[1] >= 23) or (my_lst[0] == 11 and my_lst[1] <= 21):
        output = 'scorpio'
    elif (my_lst[0] == 11 and my_lst[1] >= 22) or (my_lst[0] == 12 and my_lst[1] <= 21):
        output = 'sagittarius'
    else:
        output = None    
    return output





def get_horoscope(zodiac):
    
    """
    Generates daily horoscope based on the zodiac sign.
    
    Code modified from https://bit.ly/3pfYSJ6 and
    should be considered part of my graded work.

    Documented by me.

    Parameters
    ----------
    zodiac : str
        zodiac sign

    Returns
    -------
    str
        daily generated horoscope 
    """
  
    zodiac_vals = {'aries': 1, 'taurus': 2, 'gemini': 3, 'cancer': 4, 'leo' : 5, 'virgo': 6,
                   'libra': 7, 'scorpio' : 8, 'sagittarius' : 9, 'capricorn': 10, 
                   'aquarius': 11, 'pisces': 12}
        
    if zodiac not in zodiac_vals:
        return None

    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-today.aspx?sign={zodiac_vals[zodiac]}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    output = soup.find("div", class_="main-horoscope").p.text
    final_output = output.split('- ')
    return ' '.join(final_output[1:])





def get_lovescope(zodiac):
    
    """
    Generates daily love horoscope based on the zodiac sign.

    Code modified from https://bit.ly/3pfYSJ6 and
    should be considered part of my graded work.

    Documented by me.
    
    Parameters
    ----------
    zodiac : str
        zodiac sign

    Returns
    -------
    str
        daily generated love horoscope 
    """

    zodiac_vals = {'aries': 1, 'taurus': 2, 'gemini': 3, 'cancer': 4, 'leo' : 5, 'virgo': 6,
                   'libra': 7, 'scorpio' : 8, 'sagittarius' : 9, 'capricorn': 10, 
                   'aquarius': 11, 'pisces': 12}
        
    if zodiac not in zodiac_vals:
        return None

    url = (
        "https://www.horoscope.com/us/horoscopes/love/"
        f"horoscope-love-daily-today.aspx?sign={zodiac_vals[zodiac]}"
    )
    
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    output = soup.find("div", class_="main-horoscope").p.text
    final_output = output.split('- ')
    return ' '.join(final_output[1:])





def get_career(zodiac):
    
    """
    Generates daily career horoscope based on the zodiac sign.
    
    Code modified from https://bit.ly/3pfYSJ6 and
    should be considered part of my graded work.

    Documented by me.
    
    Parameters
    ----------
    zodiac : str
        zodiac sign

    Returns
    -------
    str
        daily generated career horoscope 
    """

    zodiac_vals = {'aries': 1, 'taurus': 2, 'gemini': 3, 'cancer': 4, 'leo' : 5, 'virgo': 6,
                   'libra': 7, 'scorpio' : 8, 'sagittarius' : 9, 'capricorn': 10, 
                   'aquarius': 11, 'pisces': 12}
        
    if zodiac not in zodiac_vals:
        return None

    url = (
        "https://www.horoscope.com/us/horoscopes/career/"
        f"horoscope-career-daily-today.aspx?sign={zodiac_vals[zodiac]}"
    )
    
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    output = soup.find("div", class_="main-horoscope").p.text
    final_output = output.split('- ')
    return ' '.join(final_output[1:])


def get_personality(input_zodiac):
    
    """
    Produces personality traits based on the zodiac sign.

    Parameters
    ----------
    input_zodiac : str
        zodiac sign

    Returns
    -------
    str or None
        Describes personality traits. None is returned if the inputed zodiac is invalid.
    """
    
    zodiac = input_zodiac.lower()
    if zodiac == 'aries':
        output = 'Aries are passionate, independent, competitive, and blunt.'
    elif zodiac == 'taurus':
        output = 'Taurus are smart, ambitious, trustworthy, and all about honesty.'
    elif zodiac == 'gemini':
        output = 'Gemini are smart, passionate, dynamic, and skilled at blending into any group dynamics.'
    elif zodiac == 'cancer':
        output = 'Cancers are emotional, intuitive, practically psychic, and standoffish.'
    elif zodiac == 'leo':
        output = 'Leos are bold, intelligent, warm, courageous, and intense.' 
    elif zodiac == 'virgo':
        output = 'Virgos are smart, sophisticated, kind, and practical.'
    elif zodiac == 'libra':
        output = 'Libras are intelligent, kind, willing to put others before themselves, and have a rich inner life.'
    elif zodiac == 'scorpio':
        output = 'Scorpios are passionate, independent, unafraid to be themselves, and love debates.'
    elif zodiac == 'sagittarius':
        output = 'Sagittarius are independent, strong-willed, adventurous, open-hearted, and generous.'
    elif zodiac == 'capricorn':
        output = 'Capricorns are smart, hardworking, in control of their destiny, and rule-followers.'
    elif zodiac == 'aquarius':
        output = 'Aquarius are independent, enigmatical, unique, and want to make the world a better place.'
    elif zodiac == 'pisces':
        output = 'Pisces are smart, creative, deeply intuitive, and sensitive.'
    else:
        output = None
    return output
    
    
def chat():
    
    '''
    
    interactive chat where a date is inputed and returns zodiac signs and various horoscopes.
    
    '''
    
    #introduction
    
    welcome = 'Hello! Welcome to the Horoscope Finder!\nThis program can help you figure out your zodiac sign, provide you with your daily horoscope, and more!\n'
    print(welcome)
    
    #converts month and day to zodiac sign 
    birth_date = input('enter a birth date (mm/dd): ')
    my_zodiac = get_monthday(birth_date) 
    
    while my_zodiac is None:
        birth_date = input('Incorrect entry. Please enter a birth date (mm/dd): ')
        my_zodiac = get_monthday(birth_date)
    

    run_chat = True
    
    #option to return a daily horoscope 
    
    while run_chat:
        produced_zodiac = get_zodiac(my_zodiac)
        if produced_zodiac is not None:
            print('Your zodiac sign is '+produced_zodiac+'\n')
        else:
            print('I was unable to get your zodiac sign!\n')
            break
                
        second_step = input('Would you like to know your daily horoscope? ')
        if second_step in ['no', 'nope', 'No', 'n', 'N']:
            run_chat = False
        else:
            daily_horoscope = get_horoscope(produced_zodiac)
            print('\n')
            print(daily_horoscope)
            print('\n')
            run_chat = False
    
    
    #option to return various types of daily horoscopes and zodiac personality traits 
    
    third_step = input('Would you like to know your horoscope for career or love, or the personality traits for your zodiac sign.\nPlease enter "career", "love", or "personality". Enter "quit" if you would like to stop the program. ')
    
    while third_step != 'quit':
        if third_step == 'career':
            produced_career = get_career(produced_zodiac)
            print('\n'+produced_career+'\n')
            third_step = input('love, personality, or quit? ')
        elif third_step == 'love':
            produced_love = get_lovescope(produced_zodiac)
            print('\n'+produced_love+'\n')
            third_step = input('career, personality, or quit? ')
        elif third_step == 'personality':
            produced_personality = get_personality(produced_zodiac)
            print('\n'+produced_personality+'\n')
            third_step = input('career, love, or quit? ')
        else:
            print('\nInvalid entry!')
            third_step = input('Please enter "career", "love", or "personality". Enter "quit" if you would like to stop the program. ')
        
    #conclusion
    
    print('\nThank you! Hope you enjoyed the Horoscope Finder!')
                
         
        

          
    
