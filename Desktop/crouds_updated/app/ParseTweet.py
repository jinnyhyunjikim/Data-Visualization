#!/usr/bin/python

import re, string

class ParseTweet(): 

    @staticmethod
    def get_one_integer(str):
    # Extracts one integer- average if two found, 
    # -1 if none or more than two found. 
        words_separated = separate_each_word(str)
        converted_to_numbers = convert_to_numbers(words_separated)
        numbers = combine_two_numbers_next_to_each_other(converted_to_numbers)
        numbers = remove_negative_numbers(numbers)
        count = len(numbers) # number of extracted
                             # 0 or positive numbers.
        
        if (count  == 0 or count > 2): return -1 # None or too many found
        if (count == 1): return numbers[0]
        if (count == 2): 
            return (numbers[0] + numbers[1]) / 2

#############################################
# spoken_word_to_number_method_1 (and helper fn's)
#############################################

# Source: http://code.activestate.com/recipes/578258-spoken-word-to-number/
_known = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
    }

def spoken_word_to_number_method_1(n):
# Assumes n is a positive integer. Returns error if not.

    if len(n) == 0: return None # added

    n = n.lower().strip()
    if n in _known:
        return _known[n]
    else:
        inputWordArr = re.split('[ -]', n)

    assert len(inputWordArr) > 1 #all single words are known
    #Check the pathological case where hundred is at the end or thousand is at end
    if inputWordArr[-1] == 'hundred':
        inputWordArr.append('zero')
        inputWordArr.append('zero')
    if inputWordArr[-1] == 'thousand':
        inputWordArr.append('zero')
        inputWordArr.append('zero')
        inputWordArr.append('zero')
    if inputWordArr[0] == 'hundred':
        inputWordArr.insert(0, 'one')
    if inputWordArr[0] == 'thousand':
        inputWordArr.insert(0, 'one')

    inputWordArr = [word for word in inputWordArr if word not in ['and', 'minus', 'negative']]
    currentPosition = 'unit'
    prevPosition = None
    output = 0
    for word in reversed(inputWordArr):
        if currentPosition == 'unit':
            number = _known[word]
            output += number
            if number > 9:
                currentPosition = 'hundred'
            else:
                currentPosition = 'ten'
        elif currentPosition == 'ten':
            if word != 'hundred':
                number = _known[word]
                if number < 10:
                    output += number*10
                else:
                    output += number
            #else: nothing special
            currentPosition = 'hundred'
        elif currentPosition == 'hundred':
            if word not in [ 'hundred', 'thousand']:
                number = _known[word]
                output += number*100
                currentPosition = 'thousand'
            elif word == 'thousand':
                currentPosition = 'thousand'
            else:
                currentPosition = 'hundred'
        elif currentPosition == 'thousand':
            assert word != 'hundred'
            if word != 'thousand':
                number = _known[word]
                output += number*1000
        else:
            assert "Can't be here" == None

    return(output)

#############################################
# get_one_integer level helper fn's
#############################################

def separate_each_word(string):
    return string.split()

def convert_to_numbers(array_of_words_and_numbers):    

    # Takes in an array of string 
    # Returns an array of the numbers each string represents. 
    # If a string does not represent a numerical value, it's converted to -1.

    array_of_numbers = []   
    for item in array_of_words_and_numbers:
        item = right_strip_punctuation(item)  
        item = left_strip_punctuation(item)  
        number = convert_word_to_number(item)
        array_of_numbers.append(number)
    return array_of_numbers

def convert_word_to_number(word_or_number):
    # Takes in a string without any whitespace or punctuation 
    # Returns the number it represents if any.
    # If not a number (int or spelled out), return -1 

    if len(word_or_number) == 0: return -1
    if word_or_number.lower() == "none": return 0
    if word_or_number.lower() == "any": return 0

    try:        # word is already a number
        number = int(word_or_number)
    except:     
        try:    # word is a number spelled out 
            number = spoken_word_to_number_method_1(word_or_number)
        except: # word is not a number
            number = -1 
    return number 

def right_strip_punctuation(word):

    # Takes in a string with no whitespace and removes all punctuation marks 
    # at the end of the string

    without_punctuation = word.rstrip(string.punctuation)
    return without_punctuation
    
def left_strip_punctuation(word):

    # Takes in a string with no whitespace and removes punctuation marks 
    # except . in the beginning of the string

    without_punctuation = word.lstrip('!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~')
    return without_punctuation

def combine_two_numbers_next_to_each_other(array_of_numbers):
    # Takes in an array of numbers and if two non-negative numbers are 
    # consecutive (a multiple of ten then a positive single digit number),
    # the two are combined. 

    new_array = []
    number_count = len(array_of_numbers)
    i = 0 
    while (i < number_count):
        number = array_of_numbers[i]
        if (number != -1 and number % 10 == 0
            and i + 1 < number_count and array_of_numbers[i + 1] != -1 and
            array_of_numbers[i + 1] < 10):
            combined_number = array_of_numbers[i] + array_of_numbers[i + 1] 
            new_array.append(combined_number) 
            i += 2
        else:
            new_array.append(number)
            i += 1
    return new_array

def remove_negative_numbers(array_of_numbers):
    # Takes in an array of zero and non-zero numbers 
    # Returns a new array of only non-negative numbers remaining 
    # in the same order

    new_array = []
    for n in array_of_numbers:
        if n >= 0:
            new_array.append(n)
    return new_array