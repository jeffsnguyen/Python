'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 5
Description: Create a simple dictionary that has country name as the key and population as the value
                (country:population). Do this for at least ten countries. Then, do the following:
                a. Create code that prompts the user for the name of a country (‘0’ to exit).
                Display the population for that country. Repeat until the user enters ‘0’.

                If the country does not exist in the dict:
                    i. Display a message to the user that the population is unknown
                        and prompt the user to enter the population.
                    ii. Update the dict with the value provided by the user.

                b. Display the final dict once the user exits the loop. Display should be in the format:
                    Country 1 has population X
                    Country 2 has population Y

                c. Note that the above display will not necessarily be sorted.
                Modify the code from part b to display sorted by 1) country then 2) population,
                largest first (Hint: Use the sorted function).

                d. Use a dict comprehension to create a sub-dictionary with countries of population
                greater than 1 billion.
'''
import pprint

def main():
    # Initialize dictionary
    country = {'Mexico': 128932753, 'India': 1380004385, 'China': 1439323776,
               'Indonesia': 273523615, 'Pakistan': 220892340, 'Brazil': 212559417,
               'Nigeria': 206139589, 'United States': 331002651,'Bangladesh': 164689383,
               'Russia': 145934462}
    # Display dictionary entries
    print('Top 10 populous countries and their population:\n')
    pprint.pprint(country)

    # Prompt user input for name of country, 0 to exit
    while True: # Loop to prompt input until break keyword (0) is entered
        country_name = input('Enter country name to lookup, 0 to exit: ')

        if country_name != '0': # Stop asking for new input once 0 is entered

            try: # Display lookup result
                print('The population of ' + country_name + ' is: ', country[country_name])
            except: # If lookup is unsuccessful, inform user
                print('Entry does not exist in dictionary. Follow prompt to update dictionary.')

                while True: # Loop to prompt input to update dictionary

                    try: # Prompt input until a valid value is found
                        new_country_pop = abs(int(input('Enter population of ' + country_name + ' :')))
                        country[country_name] = new_country_pop # Update country dict with new entry
                        # Inform user of update action
                        print('New entry recorded.\nThe population of '
                              + country_name + ' is: ', country[country_name])
                        break
                    except: # Inform user of input condition and continue the loop
                        print('Population must be a valid positive real number.')
        else:
            break # Stop prompting for input lookup

    # Unsorted printing dictionary key and its value in the format: Country 1 has population X
    print('Display dictionary, unsorted:\n')
    for country_name, pop in country.items(): # Lookup dict's key and value in country and print
        print('Country ' + country_name + ' has population ' + str(pop) + '.')

    # Sort by key & printing dictionary key and its value in the format: Country 1 has population X
    country_key_sorted = sorted(country) # Sort the key of country in alphabetical order and store in a list
    print('Display dictionary, sorted by key, alphabetical order:\n')
    # Lookup list country_key_sorted by entry which correspond to the key in the dictionary country
    # For each of the key, print the result
    for item in country_key_sorted:
        print('Country ' + item + ' has population ' + str(country[item]) + '.')

    # Sort by value & printing dictionary key and its value in the format: Country 1 has population X
    # Sort the key of country by its value (largest first) and store in a dict
    country_key_sorted = dict(sorted(country.items(), key = lambda x:x[1], reverse = True))
    print('Display dictionary, sorted by value, largest first:\n')
    # Lookup the dictionary country_key_sorted by key which correspond to the key in the dictionary country
    # For each of the key, print the result
    for country_name, pop in country_key_sorted.items():
        print('Country ' + country_name + ' has population ' + str(pop) + '.')

    # Use a dict comprehension to create a sub-dictionary with countries of population
    # greater than 1 billion.
    more_than1B = {country_name: pop for country_name, pop in country.items() if pop > 1000000000}
    print('Countries with population more than 1,000,000,000: ', more_than1B)

#######################
if __name__ == '__main__':
    main()