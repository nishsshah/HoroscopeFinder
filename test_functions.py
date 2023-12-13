import pytest
import functions


def test_get_monthday():
    assert functions.get_monthday('12/09') == [12, 9]
    assert functions.get_monthday('11/08') == [11, 8]
    assert functions.get_monthday('10/15') == [10, 15]
    assert functions.get_monthday('09/18') == [9, 18]
    assert functions.get_monthday('08/07') == [8, 7]
    assert functions.get_monthday('07/22') == [7, 22]
    assert functions.get_monthday('06/03') == [6, 3]
    assert functions.get_monthday('05/11') == [5, 11]
    assert functions.get_monthday('04/30') == [4, 30]
    assert functions.get_monthday('03/25') == [3, 25]
    assert functions.get_monthday('02/14') == [2, 14]
    assert functions.get_monthday('01/01') == [1, 1]
    assert type(functions.get_monthday('12/09')) == list
    assert functions.get_monthday('1/1') == None
    
    
def test_get_zodiac():
    assert functions.get_zodiac([12, 9]) == 'sagittarius'
    assert functions.get_zodiac([1, 10]) == 'capricorn'
    assert functions.get_zodiac([2, 18]) == 'aquarius'
    assert functions.get_zodiac([3, 1]) == 'pisces'
    assert functions.get_zodiac([4, 12]) == 'aries'
    assert functions.get_zodiac([5, 11]) == 'taurus'
    assert functions.get_zodiac([6, 2]) == 'gemini'
    assert functions.get_zodiac([6, 24]) == 'cancer'
    assert functions.get_zodiac([8, 22]) == 'leo'
    assert functions.get_zodiac([9, 17]) == 'virgo'
    assert functions.get_zodiac([10, 2]) == 'libra'
    assert functions.get_zodiac([11, 15]) == 'scorpio'
    assert functions.get_zodiac('') == None
    assert functions.get_zodiac([15, 11]) == None
    

def test_get_horoscope():
    assert type(functions.get_horoscope('sagittarius')) == str
    assert type(functions.get_horoscope('capricorn')) == str
    assert type(functions.get_horoscope('aquarius')) == str
    assert type(functions.get_horoscope('pisces')) == str
    assert type(functions.get_horoscope('aries')) == str
    assert type(functions.get_horoscope('taurus')) == str
    assert type(functions.get_horoscope('gemini')) == str
    assert type(functions.get_horoscope('cancer')) == str
    assert type(functions.get_horoscope('leo')) == str
    assert type(functions.get_horoscope('virgo')) == str
    assert type(functions.get_horoscope('libra')) == str
    assert type(functions.get_horoscope('scorpio')) == str
    assert functions.get_horoscope('') == None
                

def test_get_lovescope():
    assert type(functions.get_lovescope('sagittarius')) == str
    assert type(functions.get_lovescope('capricorn')) == str
    assert type(functions.get_lovescope('aquarius')) == str
    assert type(functions.get_lovescope('pisces')) == str
    assert type(functions.get_lovescope('aries')) == str
    assert type(functions.get_lovescope('taurus')) == str
    assert type(functions.get_lovescope('gemini')) == str
    assert type(functions.get_lovescope('cancer')) == str
    assert type(functions.get_lovescope('leo')) == str
    assert type(functions.get_lovescope('virgo')) == str
    assert type(functions.get_lovescope('libra')) == str
    assert type(functions.get_lovescope('scorpio')) == str
    assert functions.get_lovescope('') == None

def test_get_career():
    assert type(functions.get_career('sagittarius')) == str
    assert type(functions.get_career('capricorn')) == str
    assert type(functions.get_career('aquarius')) == str
    assert type(functions.get_career('pisces')) == str
    assert type(functions.get_career('aries')) == str
    assert type(functions.get_career('taurus')) == str
    assert type(functions.get_career('gemini')) == str
    assert type(functions.get_career('cancer')) == str
    assert type(functions.get_career('leo')) == str
    assert type(functions.get_career('virgo')) == str
    assert type(functions.get_career('libra')) == str
    assert type(functions.get_career('scorpio')) == str
    assert functions.get_career('') == None

def test_get_personality():
    assert type(functions.get_personality('sagittarius')) == str
    assert type(functions.get_personality('capricorn')) == str
    assert type(functions.get_personality('aquarius')) == str
    assert type(functions.get_personality('pisces')) == str
    assert type(functions.get_personality('aries')) == str
    assert type(functions.get_personality('taurus')) == str
    assert type(functions.get_personality('gemini')) == str
    assert type(functions.get_personality('cancer')) == str
    assert type(functions.get_personality('leo')) == str
    assert type(functions.get_personality('virgo')) == str
    assert type(functions.get_personality('libra')) == str
    assert type(functions.get_personality('scorpio')) == str
    assert functions.get_personality('') == None

