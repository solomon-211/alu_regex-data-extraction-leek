# Regex Data Extraction Tool

This Python project basically elaborates how to extract different data types from the string of texts using the regular expressions(regex)

## Data type to be extracted from the string of texts

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time formats (12-hour and 24-hour)

## Python programming languages used to build, encompasses;
importing modules
- This is to find the matching pattern for the regular expressions and given them a current timestamp
Dictionaries
- A dictionary is used to store different regex patterns and their descriptions to later access the data type need to be extracted.
Raw Strings for Regex
- The r'' prefix stands for raw string, which directs Python not to escape backslashes — important for regex patterns to matching their correspomding data type.
Multiline Strings
- To show the multiple line of codes wrapped up in a docstring and stores the data


"""Contact us at john.doe@example.com or jane.smith@company.co.uk.
Visit our site at https://www.example.com or https://subdomain.example.org/page.
Call us at (123) 456-7890, 987-654-3210, or 123-456-7890.
Use credit card 1234 5678 9012 3456 or 1234-5678-9012-3456 to pay.
Our office hours are 9:00 AM to 5:30 PM, and the server backup runs at 23:45.
Meeting scheduled for 14:30 tomorrow."""
Functions
- Functions are used to organize logic in order to extract data and display the data extracted.
REGEX DATA EXTRACTION RESULTS (2025-09-19 14:40:52)
🔹 EMAILS
  1. john.doe@example.com
  2. jane.smith@company.co.uk

🔹 URLS
  1. https://www.example.com
  2. https://subdomain.example.org/page.

🔹 PHONES
  1. (123) 456-7890
  2. 987-654-3210
  3. 123-456-7890

🔹 CREDIT_CARDS
  1. 1234 5678 9012 3456
  2. 1234-5678-9012-3456

🔹 TIMES
  1. 9:00 AM
  2. 5:30 PM
  3. 23:45
  4. 14:30
for Loops and .items()
-This iterates in each patterns and returns the all possible matches patterns.
Sets or Dicts for Removing Duplicates
- This ensures that there are no available duplicates in *sets* or *dicts* and convert back to the list.
Conditionals
- It validates the results before printing them
Datetime Formatting
- This ensures that the timestamp display to be the current or exact time for running code.
Main Guard
- This program ensures the project run successfully.

