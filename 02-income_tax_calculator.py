#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate Income tax

# We will assume Normal user (not a senior citizen / NRI)
income = float(input("Enter the income: "))
# Simple Slab Calculation
# > 5L and < 10L : 5% Tx
# >= 10L and <= 20L : 10% Tax
# >= 20L : 30% Tax
# income_tax = 0
if income > 5_00_000 and income < 10_00_000:
    income_tax = income * (5/100)
elif income >= 10_00_000 and income <= 20_00_000:
    income_tax = income * (10/100)
elif income > 20_00_000:
    income_tax = income * (30/100)
else:
    income_tax = 0

print(f'Tax on {income} is {income_tax}')