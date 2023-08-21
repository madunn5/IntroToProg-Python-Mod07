# ------------------------------------------------- #
# Title: Assignment 07 - Pickling
# Description: A simple example of storing data in a binary file
#              and then using pickle to unpickle it. Additionally,
#              the program can print the data to a text file,
#              delete all previously saved data and show the user
#              the binary data
# ChangeLog: (Who, When, What)
# MDunn,8/17/2023,Created Script
# ------------------------------------------------- #

import pickle

# Data -------------------------------------------- #
user_id = ''  # Captures the user ID input
user_name = ''  # Captures the username input
user_data = []  # A list that acts as a table of rows
filename_pickle = 'data.pkl'  # The name of the binary file used for pickling data
filename_txt = 'data.txt'  # The name of the text file that will show the data in plain english
choiceStr = ''  # Captures the choice made from the option menu
data_list = []  # A list that acts as the data currently in the program


# Processing -------------------------------------- #
class Processor:
    """ Performs processing tasks, such as saving data, reading data, and deleting data"""

    @staticmethod
    def save_pickled_data_to_file(data, filename):
        """ Saves current data using pickle.dump()

                :param data: (string) with data to save
                :param filename: (string) with name of file
                :return: nothing
                """
        try:
            with open(filename, 'ab') as file:
                pickle.dump(data, file)
            print()  # space for formatting
            print(f"Data saved to {filename} successfully.")
        except Exception as e:
            print(f"Error while saving data: {e}")

    @staticmethod
    def save_unpickled_data_to_file(data, filename):
        """ Saves current data to text file. Because we are using read_pickled_data_from_file in order
        to create the data_list variable, the data is automatically printed to the screen, allowing the
        user to see what is being saved to the text file

                :param data: (string) with data to save
                :param filename: (string) with name of file
                :return: nothing
                """
        try:
            with open(filename, 'w') as file:
                if data:
                    file.write('user_id,user_name\n')  # Adds user_id and user_name as a header for each column
                    for row in data:
                        file.write(row[0] + ',' + row[1] + '\n')
                    print()  # space for formatting
                    print(f'The above data has been saved to {filename}!\n')
                else:
                    print('No data to save.\n')
        except Exception as e:
            print(f"Error while saving data: {e}")

    @staticmethod
    def read_pickled_data_from_file(filename):
        """ Reads pickled data from a file and returns it in plain english

                :param filename: (string) with name of file
                :return: (list) of data read from the file
                """
        try:
            with open(filename, 'rb') as file:
                data_list = []
                while True:
                    try:
                        user_data = pickle.load(file)
                        data_list.append(user_data)
                    except EOFError:  # this is an end-of-line error which triggers the break in the loop
                        break
                if data_list:  # if the data_list exists, this loop will run
                    for row in data_list:
                        print(row[0], row[1], sep=',')
                else:
                    print('No data is available.')
                return data_list
        except Exception as e:
            print(f"Error while reading data: {e}")
            return None

    @staticmethod
    def delete_pickled_data_from_file(filename):
        """ Deletes the previously saved data

                :param filename: (string) with name of file
                :return: nothing
                """
        try:
            with open(filename, 'wb'):
                pass
            print(f"All data has been deleted from {filename} successfully.")
        except Exception as e:
            print(f"Error while saving data: {e}")

    @staticmethod
    def read_pickled_data_as_binary(filename):
        """ Returns pickled data in binary to the user, so they can see what it looks like

                :param filename: (string) with name of file
                :return: (bytes) of binary data read from the file
                """
        try:
            with open(filename, 'rb') as file:
                binary_data = file.read()
                print('Below is what your data looks like in binary!', '\n')
                print(binary_data)
        except Exception as e:
            print(f"Error while reading data: {e}")
            return None


class InputOutput:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_choices():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show Current Data
            2) Add New Data
            3) Create a New File/Delete Existing Data
            4) Show Binary Data
            5) Save Data to Text File       
            6) Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_new_user_id_and_user_name():
        """  Gets user_id and user_name values to be added to the list

        :return: (string, string) with user_id and user_name
        """
        # if the input is not a number, the code will repeat until a valid input is received
        while True:
            user_id = input('Enter an ID: ')
            if user_id.isnumeric():
                break
            else:
                print('Please only use numbers for the User\'s ID!')

        # if the user_name is blank the code will ask for a valid input
        while True:
            user_name = input("Enter a name: ")
            if user_name.strip():
                break
            else:
                print('User name cannot be blank')
        user_data = [user_id, user_name]
        return user_data


# Presentation ------------------------------------ #
while True:
    InputOutput.output_menu_choices()  # Shows menu of options
    choice_str = InputOutput.input_menu_choice()  # Get menu option

    if choice_str.strip() == '1':  # View current data
        print('user_id,user_name')
        Processor.read_pickled_data_from_file(filename=filename_pickle)
        continue  # to show the menu

    elif choice_str == '2':  # Add and save data
        user_data = InputOutput.input_new_user_id_and_user_name()
        Processor.save_pickled_data_to_file(data=user_data, filename=filename_pickle)
        continue  # to show the menu

    elif choice_str == '3':  # Overwrite the file, starts with user_id and user_name at top for formatting
        Processor.delete_pickled_data_from_file(filename=filename_pickle)
        continue  # to show the menu

    elif choice_str == '4':  # View the binary data
        Processor.read_pickled_data_as_binary(filename=filename_pickle)
        continue

    elif choice_str == '5':  # Add and save data
        data_list = Processor.read_pickled_data_from_file(filename=filename_pickle)
        Processor.save_unpickled_data_to_file(data=data_list, filename=filename_txt)
        continue

    elif choice_str == '6':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

    else:
        print('Please choose a number between 1 and 6!')
