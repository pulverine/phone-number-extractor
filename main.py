import re
import openpyxl

# List of all country phone numbers scrap-able
country_list = ['AF', 'AR', 'AU', 'BD', 'BR', 'CA', 'CN', 'EG', 'FR', 'DE', 'IN', 'ID', 'ID', 'IR',
                'IQ', 'IT', 'NG', 'MX', 'PK', 'PH', 'RU', 'ZA', 'ES', 'TR', 'UK', 'US']
print(country_list)

ng_list = []
us_list = []


# This function locates all the numbers matching the appropriate regular expression for phone numbers from the specified country

def check_another():
    answer = input('Do you want to check for another country number? Y/N')
    if answer == 'Y':
        scrap_numbers()
    else:
        pass


def scrap_numbers():
    # Input the 2 letter abbreviation of the country
    country = input('Select country from the list of specified: ')

    # Open txt file to scrap.
    with open('sample.txt', 'r', encoding='utf-8') as file:
        for line in file:
            ng_match1 = re.search(r"070\d{8}", line)
            ng_match2 = re.search(r'070\d\s\d{4}\s\d{3}', line)
            ng_match3 = re.search(r'070\d\s\d{3}\s\d{4}', line)
            ng_match4 = re.search(r'070\s\d{4}\s\d{4}', line)

            ng_match5 = re.search(r"071\d{8}", line)
            ng_match6 = re.search(r'071\d\s\d{4}\s\d{3}', line)
            ng_match7 = re.search(r'071\d\s\d{3}\s\d{4}', line)
            ng_match8 = re.search(r'071\s\d{4}\s\d{4}', line)

            ng_match9 = re.search(r"080\d{8}", line)
            ng_match10 = re.search(r'080\d\s\d{4}\s\d{3}', line)
            ng_match11 = re.search(r'080\d\s\d{3}\s\d{4}', line)
            ng_match12 = re.search(r'080\s\d{4}\s\d{4}', line)

            ng_match13 = re.search(r"081\d{8}", line)
            ng_match14 = re.search(r'081\d\s\d{4}\s\d{3}', line)
            ng_match15 = re.search(r'081\d\s\d{3}\s\d{4}', line)
            ng_match16 = re.search(r'081\s\d{4}\s\d{4}', line)

            ng_match17 = re.search(r"090\d{8}", line)
            ng_match18 = re.search(r'090\d\s\d{4}\s\d{3}', line)
            ng_match19 = re.search(r'090\d\s\d{3}\s\d{4}', line)
            ng_match20 = re.search(r'090\s\d{4}\s\d{4}', line)

            ng_match21 = re.search(r"091\d{8}", line)
            ng_match22 = re.search(r'091\d\s\d{4}\s\d{3}', line)
            ng_match23 = re.search(r'091\d\s\d{3}\s\d{4}', line)
            ng_match24 = re.search(r'091\s\d{4}\s\d{4}', line)

            ng_match25 = re.search(r"\+234\s\d{3}\s\d{3}\s\d{4}", line)
            ng_match26 = re.search(r"\+234\s\d{3}\s\d{4}\s\d{3}", line)
            ng_match27 = re.search(r"\+234\s\d{4}\s\d{3}\s\d{3}", line)
            ng_match28 = re.search(r"\+234\d{10}", line)

            us_match1 = re.search(r"^\+1\s\d{3}-\d{3}-\d{4}$", line)
            us_match2 = re.search(r"^\+1\s\d{3}\s\d{3}\s\d{4}$", line)
            us_match3 = re.search(r"^\+1\d{10}$", line)

            # Check if the inputted country is among specified countries
            if country.upper() in country_list:

                if country.upper() == 'NG':
                    # Specify regular expressions for the country phone numbers

                    ng_match_list = [ng_match1, ng_match2, ng_match3, ng_match4, ng_match5, ng_match6, ng_match7,
                                     ng_match8, ng_match9, ng_match10,
                                     ng_match11, ng_match12, ng_match13,
                                     ng_match14, ng_match15, ng_match16, ng_match17, ng_match18, ng_match19, ng_match20,
                                     ng_match21, ng_match22,
                                     ng_match23, ng_match24, ng_match25,
                                     ng_match26, ng_match27, ng_match28]

                    for match in ng_match_list:
                        if match:
                            ng_list.append(match.group())
                        else:
                            pass

                    print(f'Nigerian Numbers: {ng_list}')

                if country.upper() == 'US':

                    us_match_list = [us_match1, us_match2, us_match3,
                                     # us_match4, us_match5, us_match6, us_match7, us_match8,
                                     # us_match9, us_match10,
                                     # us_match11, us_match12, us_match13,
                                     # us_match14, us_match15, us_match16, us_match17, us_match18, us_match19, us_match20,
                                     # us_match21, us_match22,
                                     # us_match23, us_match24, us_match25,
                                     # us_match26, us_match27, us_match28
                                     ]

                    for match in us_match_list:
                        if match:
                            us_list.append(match.group())
                        else:
                            pass

                    print(f'US Numbers: {us_list}')

                check_another()
            else:
                print('Please enter a valid country from the list')
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


scrap_numbers()
