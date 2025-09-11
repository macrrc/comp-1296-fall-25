"""
chris_mac_assignment_1.py
Assignment 1 - Student Data Collector
Bare Minimum Solution
"""

# Collect Information
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
weekly_study_hours = float(input("Enter hours you study per week: "))

# Perform Calculations
age_in_months = user_age * 12
study_hours_per_day = weekly_study_hours / 7

# Display Results
print("\n--- Summary Report ---")
print("Hello,", user_name + "!")
print("You are", user_age, "years old, which is about", age_in_months, "months.")
print(f"You study around {study_hours_per_day:.2f} hours per day on average.")