"""
script file with two functions
one to calculate degree fahrenheit to degree celsius
one to classify degree celsius
"""

# function calculating fahrenheit to celsius
def fahr_to_celsius(temp_fahrenheit):
    """
    Function to calculate degree Farenheit to degree Celsius
    temp_farenheit is number of degree Farenheit that should be calculated
    returns this number in degree Celsius
    """
    return (temp_fahrenheit - 32) / 1.8

#function classifying degree celsius
def temp_classifier(temp_celsius):
    """
    Function to classify degree Celsius
    parameter temp_celsius is input, that should be classified
    returns class 0-3 depending on which temperature range corresponds
    """
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    else:
        return 3