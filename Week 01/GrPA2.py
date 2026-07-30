'''
Solve all the below tasks related to relational and logical operators.

This exercise gives you practice in building up boolean expressions.

Problem Type: Input variable - Output Variable, Hidden suffix for evaluation
'''

"""
Instructions on how to solve :
NOTE: In this type of questions you should not take input or print anything unless your are explicitly asked to. Assign the result of the required computation to the correct variable name as it will be evaluated for type and value by the evaluator.

The input variables will be assigned by the evaluator based on the test cases.

The grey part before the white part (if any) in the code is the prefix code. The grey part after the white part (if any) is the suffix code which are not editable. Usually they will be the part of code but in this type of questions it will be removed by the evaluator.

The Three dots (...) called as Ellipsis in python are like placeholders, replace them with your answer.

The inputs on the code blocks are just sample inputs they won't be evaluated in the actual testcases.

Each testcase will have its own set of testcases defined as variables. The check function in the testcases is in the hidden evaluation code that checks the value and type of the variable.



Template Code:
output1 = ... # bool: True if a greater than or equal to 5

output2 = ... # bool: True if a is divisible by 5

output3 = ... # bool: True if a is odd number less than 10

output4 = ... # bool: True if a is an odd number within the range -10 and 10

output5 = ... # bool: True if a has even number of digits but not more than 10 digits

is_offer1_cheaper = ... # bool: True if the offer1 is strictly cheaper
"""

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
a = 5

price1, discount1 = 50, 4 # for offer1
price2, discount2 = 60, 8 # for offer2

# Assume discount is given in percentages

# <eoi>

output1 = a>=5 # bool: True if a greater than or equal to 5

output2 = a%5==0 # bool: True if a is divisible by 5

output3 = (a%2==1) and a<10 # bool: True if a is odd number less than 10

output4 = (a%2==1) and a>-10 and a<10 # bool: True if a is an odd number within the range -10 and 10

output5 = len(str(a))<=10 and len(str(a))%2==0 # bool: True if a has even number of digits but not more than 10 digits

is_offer1_cheaper = (price1-((price1*discount1)/100))<(price2-((price2*discount2)/100)) # bool: True if the offer1 is strictly cheaper
