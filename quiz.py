#!/usr/bin/env python3
import random as rand
import time
import os

from countryinfo import CountryInfo
os.system('clear')

start_time = time.time()

countries = [
    "Afghanistan", "Albania", "Algeria", "American Samoa", "Angola",
    "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba",
    "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
    "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia",
    "Cameroon", "Canada", "Cape Verde", "Cayman Islands",
    "Central African Republic", "Chad", "Chile", "China", "Christmas Island",
    "Cocos (Keeling) Islands", "Colombia", "Comoros",
    "Democratic Republic of the Congo", "Republic of the Congo",
    "Cook Islands", "Costa Rica", "Ivory Coast", "Croatia", "Cuba", "Cyprus",
    "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
    "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji",
    "Finland", "France", "French Polynesia", "Gabon", "The Gambia", "Georgia",
    "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada",
    "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hong Kong", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy",
    "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "South Korea", "South Korea", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
    "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali",
    "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mayotte",
    "Mexico", "Federated States of Micronesia", "Moldova", "Monaco", "Mongolia",
    "Montserrat", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger",
    "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway",
    "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Pitcairn Islands", "Poland", "Portugal",
    "Puerto Rico", "Qatar", "Romania", "Russia", "Rwanda", "Saint Helena",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Saudi Arabia",
    "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau",
    "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
    "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam",
    "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"
    ]

choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

categories = [
    "area" , "subregion", "calling code", "population", "capital", "currency",
    "latitude", "longitude"
    ]

options = [3, 6, 2, 3, 8, 4, 3, 3]

subregions = [
    'Western Europe', 'Eastern Europe', 'Southern Asia', 'Northern Africa',
    'Eastern Asia', 'South America', 'Middle Africa', 'Melanesia',
    'Central America', 'Australia and New Zealand', 'Northern America',
    'Polynesia', 'Eastern Africa', 'Western Asia', 'South-Eastern Asia',
    'Northern Europe', 'Southern Europe', 'Central Asia', 'Southern Africa',
    'Caribbean', 'Western Africa', 'Micronesia'
    ]

currencies = [
    'NZD', 'MNT', 'BND', 'GIP', 'TTD', 'NOK', 'CNY', 'MWK', 'BDT', 'USD', 'CVE',
    'PEN', 'SYP', 'AUD', 'MUR', 'AED', 'FKP', 'LBP', 'JMD', 'ILS', 'VEF', 'ISK',
    'GTQ', 'MRO', 'AMD', 'TND', 'BYR', 'KRW', 'COP', 'AOA', 'LAK', 'SAR', 'CHE',
    'GNF', 'CDF', 'DJF', 'BWP', 'TMT', 'NIO', 'KZT', 'GYD', 'NPR', 'TOP', 'KHR',
    'XAF', 'EUR', 'PLN', 'JOD', 'SDB', 'IDR', 'BZD', 'TRY', 'PAB', 'CZK', 'SDG',
    'PHP', 'BHD', 'HRK', 'UZS', 'BTN', 'GHS', 'KMF', 'DZD', 'KGS', 'NGN', 'RON',
    'TJS', 'BMD', 'CLF', 'PKR', 'RUB', 'AZN', 'XCD', 'OMR', 'LKR', 'ERN', 'EGP',
    'CRC', 'MZN', 'BBD', 'UGX', 'TWD', 'WST', 'VUV', 'KYD', 'ZMK', 'FJD', 'SVC',
    'MXN', 'MGA', 'BGN', 'ZAR', 'MYR', 'HNL', 'MVR', 'PYG', 'IRR', 'SOS', 'MDL',
    'DKK', 'UYI', 'KWD', 'GMD', 'BAM', 'SRD', 'BRL', 'TZS', 'INR', 'MAD', 'QAR',
    'XPF', 'KES', 'CHF', 'SEK', 'IQD', 'SCR', 'LSL', 'SZL', 'ARS', 'HTG', 'SGD',
    'BIF', 'CUC', 'THB', 'XOF', 'SHP', 'YER', 'VND', 'PGK', 'HKD', 'RWF', 'NAD',
    'ALL', 'BSD', 'LYD', 'ETB', 'DOP', 'GBP', 'BOB', 'CAD', 'JPY', 'SLL', 'AFN',
    'UAH', 'LRD', 'GEL', 'AWG'
    ]

print("------------------------")
print("WELCOME TO THIS QUIZ !!!")
print("------------------------\n")

print("In this game your knowledge of countries will be tested.")
print("The questions will be asked from the following categories including:")
for i in categories:
    index = categories.index(i)
    print("(" +str(choices[index])+ ") " +i)

print("\nWould you like all categories to be included?")
check = input("Press 'y' for yes or 'n' for no: ")
while check != "y" and check != "n":
    check = input("Please press 'y' for yes or 'n' for no: ")


if check == "n":
    print("\nPlease select the relevant categories.")
    categories_remove = []
    options_remove = []

    for i in categories:
        index = categories.index(i)
        print('\nWould you like ' +i+ ' to be included?')
        check = input("Press 'y' for yes or 'n' for no: ")

        while check != "y" and check != "n":
            check = input("Please press 'y' for yes or 'n' for no: ")

        if check == "n":
            categories_remove.append(i)
            options_remove.append(index)

    for i in categories_remove:
        categories = [x for x in categories if x != i]

    options = [i for j, i in enumerate(options) if j not in options_remove]

questions = int(input("\nPlease enter the number of questions you want to play for ranging from 5 to 100: "))

while questions < 5 or questions > 100:
    questions = int(input("Please enter the number of questions you want to play for ranging from" "5 to 100: "))


os.system('clear')

countries_question = rand.sample(countries, questions)
score = 0

for i in range(0, questions):
    category = rand.choice(categories)
    category_index = categories.index(category)

    print("Q" +str(i+1)+ ". What is the " +category+ " of " +countries_question[i]+ "?")

    country = CountryInfo(countries_question[i])
    country_pool = countries
    country_pool = [x for x in country_pool if x != countries_question[i]]
    country_pool = rand.sample(country_pool, options[category_index]-1)
    country_pool.append(countries_question[i])
    rand.shuffle(country_pool)

    if  category == "subregion":
        subregion_pool = subregions
        subregion_pool = [y for y in subregion_pool if y != country.subregion()]
        subregion_pool = rand.sample(subregion_pool, options[category_index]-1)
        subregion_pool.append(country.subregion())
        rand.shuffle(subregion_pool)
        index = subregion_pool.index(country.subregion())

    elif category == "currency":
        currencies_pool = currencies
        currencies_pool = [y for y in currencies_pool if y != country.currencies()[0]]
        currencies_pool = rand.sample(currencies_pool, options[category_index]-1)
        currencies_pool.append(country.currencies()[0])
        rand.shuffle(currencies_pool)
        index = currencies_pool.index(country.currencies()[0])

    else:
        index = country_pool.index(countries_question[i])

    answer = choices[index]

    for x in range(options[category_index]):
        country_choice = CountryInfo(country_pool[x])

        if category == "area":
            print ('(' +choices[x]+ ') ' +str(country_choice.area())+ " sq kilometers")

        elif category == "subregion":
            print ('(' +choices[x]+ ') ' +subregion_pool[x])

        elif  category == "calling code":
            print ('(' +choices[x]+ ') ' +str(country_choice.calling_codes()[0]))

        elif  category == "population":
            print ('(' +choices[x]+ ') ' +str(country_choice.population()))

        elif  category == "capital":
            print ('(' +choices[x]+ ') ' +country_choice.capital())

        elif  category == "currency":
            print ('(' +choices[x]+ ') ' +currencies_pool[x])

        elif  category == "latitude":
            print ('(' +choices[x]+ ') ' +str(country_choice.latlng()[0]))

        elif  category == "longitude":
            print ('(' +choices[x]+ ') ' +str(country_choice.latlng()[1]))

    answer_user = input("\nPlease choose an option: ")
    while answer_user not in choices[0:options[category_index]]:
        answer_user = input("Please choose a valid option: ")

    if answer_user == answer:
        print("\nCorrect answer !!!")
        score = score+1
    else:
        print("\nWrong answer !!!")


    if  category == "area":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.area())+ " square kilometers.")

    elif category == "subregion":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.subregion())+ ".")

    elif category == "calling code":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.calling_codes()[0])+ ".")

    elif category == "population":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.population())+ ".")

    elif category == "capital":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.capital())+ ".")

    elif category == "currency":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.currencies()[0])+ ".")

    elif category == "latitude":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.latlng()[0])+ ".")

    elif category == "longitude":
        print("The " +category+ " of " +countries_question[i]+ " is " +str(country.latlng()[1])+ ".")

    percentage = score/(i+1)*100
    print("Your score is " +str(percentage)+ "%.")
    input("\nPress any key to continue to next question...")
    os.system('clear')

print("Your final score is " +str(score/(i+1)*100)+ " %.")

if percentage < 50:
    print("\nSorry you have failed this test :-(\nBetter luck next time !\n")
elif percentage >= 50 and percentage < 60:
    print("\nCongratulations !!!\nYou have barely passed this test.\n")
elif percentage >= 60 and percentage < 85:
    print("\nCongratulations !!!\nYou have passed this test.\n")
elif percentage >= 85 and percentage < 95:
    print("\nCongratulations !!!\nYou have passed this test with flying colors !!!.\n")
elif percentage >= 95:
    print("\nCongratulations !!!\nYou have passed this test with distinction !!!\n")

print ('The game lasted ' +str(time.time()-start_time)+ ' seconds!')