# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 15:54:25 2022

@author: steve
"""

#Exercice 1
'''Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
------------
The function name : create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
-----------
BE CAREFULL WE WANT EXACTLY THE FORMAT BELOW
=> returns "(123) 456-7890"
----------- 
 '''




################# Solution ###################


def create_phone_number(n):
    '''    

    Parameters
    ----------
    n : This is the phone number enter by the user.

    Returns
    -------
    number : This function returns a string of numbers in the form of a phone number.

    '''
    # I create 3 lists for each part of the phone number
    #the first part has 3 numbers
    number1 =n[:3] 
    #the second part has 3 numbers
    number2=n[3:6]
    #the third part has 4 numbers
    number3 = n[6:]
    
    '''Now that I separate the list into 3 lists we are going to
    change each list into a string and concatenate everything together.
    You can use different methods but i usually use "{}" + format
    What we want to get => "(123) 456-7890"
    To get this result we will use the method join + a one line loop
    to transform our lists into str
    '''
    number1 = ''.join(str(e) for e  in number1)  
    number2 = ''.join(str(e) for e  in number2)  
    number3 = ''.join(str(e) for e  in number3)
    
    number ='({}) {}-{}'.format(number1, number2, number3)
    return number 
"""We could have done it in less lines but for education purposes i prefered 
    separate each step.
"""
create_phone_number([1,2,3,4,5,6,7,8,9,0])



