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
            if country.upper() in country_list:
                # Specify regular expressions for the country phone numbers
                match1 = re.search(r"070\d{8}", line)
                match2 = re.search(r'070\d\s\d{4}\s\d{3}', line)
                match3 = re.search(r'070\d\s\d{3}\s\d{4}', line)
                match4 = re.search(r'070\s\d{4}\s\d{4}', line)

                match5 = re.search(r"071\d{8}", line)
                match6 = re.search(r'071\d\s\d{4}\s\d{3}', line)
                match7 = re.search(r'071\d\s\d{3}\s\d{4}', line)
                match8 = re.search(r'071\s\d{4}\s\d{4}', line)

                match9 = re.search(r"080\d{8}", line)
                match10 = re.search(r'080\d\s\d{4}\s\d{3}', line)
                match11 = re.search(r'080\d\s\d{3}\s\d{4}', line)
                match12 = re.search(r'080\s\d{4}\s\d{4}', line)

                match13 = re.search(r"081\d{8}", line)
                match14 = re.search(r'081\d\s\d{4}\s\d{3}', line)
                match15 = re.search(r'081\d\s\d{3}\s\d{4}', line)
                match16 = re.search(r'081\s\d{4}\s\d{4}', line)

                match17 = re.search(r"090\d{8}", line)
                match18 = re.search(r'090\d\s\d{4}\s\d{3}', line)
                match19 = re.search(r'090\d\s\d{3}\s\d{4}', line)
                match20 = re.search(r'090\s\d{4}\s\d{4}', line)

                match21 = re.search(r"091\d{8}", line)
                match22 = re.search(r'091\d\s\d{4}\s\d{3}', line)
                match23 = re.search(r'091\d\s\d{3}\s\d{4}', line)
                match24 = re.search(r'091\s\d{4}\s\d{4}', line)

                match25 = re.search(r"\+234\s\d{3}\s\d{3}\s\d{4}", line)
                match26 = re.search(r"\+234\s\d{3}\s\d{4}\s\d{3}", line)
                match27 = re.search(r"\+234\s\d{4}\s\d{3}\s\d{3}", line)
                match28 = re.search(r"\+234\d{10}", line)

                match_list = [match1, match2, match3, match4, match5, match6, match7, match8, match9, match10, match11, match12, match13,
                              match14, match15, match16, match17, match18, match19, match20, match21, match22, match23, match24, match25,
                              match26, match27, match28]

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



