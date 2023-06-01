import re
import openpyxl
# List of all country phone numbers scrap-able
country_list = ['AF', 'AR', 'AU', 'BD', 'BR', 'CA', 'CN', 'EG', 'FR', 'DE', 'IN', 'ID', 'ID', 'IR',
                'IQ', 'IT', 'NG', 'MX', 'PK', 'PH', 'RU', 'ZA', 'ES', 'TR', 'UK', 'US']
print(country_list)

ng_list = []

# This function locates all the numbers matching the appropriate regular expression for phone numbers from the specified country
def scrap_numbers():
    # Input the 2 letter abbreviation of the country
    country = input('Select country from the list of specified: ')

    # Open txt file to scrap.
    with open('sample.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # Check if the inputted country is among specified countries
            if country == 'NG':
                # Specify regular expressions for the country phone numbers
                match1 = re.search(r'070\d\d\d\d\d\d\d\d', line)
                match2 = re.search(r'071\d\d\d\d\d\d\d\d', line)
                match3 = re.search(r'080\d\d\d\d\d\d\d\d', line)
                match4 = re.search(r'081\d\d\d\d\d\d\d\d', line)
                match5 = re.search(r'090\d\d\d\d\d\d\d\d', line)
                match6 = re.search(r'091\d\d\d\d\d\d\d\d', line)
                match7 = re.search(r"\+234\s\d{3}\s\d{3}\s\d{4}", line)
                match8 = re.search(r"\+234\d{3}\d{3}\d{4}", line)
                match_list = [match1, match2, match3, match4, match5, match6, match7, match8]

                for match in match_list:
                    if match:
                        ng_list.append(match.group())

            elif country == 'US':
                # Open txt file to scrap.
                pass
            else:
                print('Please enter a country from the specified list.')
                scrap_numbers()

    # Create a new workbook
    workbook = openpyxl.Workbook()

    # Select the active sheet
    sheet = workbook.active

    # Define your array

    # Write the array values to the column in Excel
    for index, value in enumerate(ng_list):
        sheet.cell(row=index + 1, column=1, value=value)

    # Save the workbook
    workbook.save("output.xlsx")

    print(f'Nigerian Numbers: {ng_list}')




scrap_numbers()



