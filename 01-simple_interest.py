#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate Simple Interest v1.0
# si = ptr / 100

principal = int(input('Enter the principal amount: '))  # Principal amount
time_in_months = int(input('Enter the time in months(Eg: 3yrs -> 36): '))
rate_of_interest = float(input('Enter the rate of interst in percentage(Eg: 7% -> 0.07): '))

simple_interest = principal * time_in_months * rate_of_interest
# print('The simple interest is:',simple_interest, sep='...', end='')
# print('The simple interest is:'+str(simple_interest))
# print('The simple interest is: %.2f'%(simple_interest))
# print('The simple interest is:{0}'.format(simple_interest))
print(f'The simple interest is:{simple_interest: .2f}')