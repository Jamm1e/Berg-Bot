import pandas as pd
from datetime import datetime

info_track = {"first_name": 0,"last_name": 1, "birth_date": 2, "email": 3, "address": 4, "entry_term": 5, "major": 6, "gpa": 7}

try:
    df = pd.read_csv('sample_responses.csv', delimiter=',')
except FileNotFoundError:
    print("File Not Found. Berg-Bot can't talk :(\n")
    exit() # since there is no file, Berg-Bot cant talk

class Berg_Bot:
    """ 
    Get keywords and responses from CSV file (BERGBOT) to assist user 
    """
    def __init__(self, info):
        self.info = info

    def get_info(self):
        return self.info   

    def set_info(self, new_info):
        self.info = new_info
        return self.info   

    # Finds keyword and returns a corresponding response
    def lookUp_keyword(self):
        try:
            question = input(f"What do you need help with relating to your {' '.join(self.get_info().split('_'))}? --> ").lower()
            keywords = [word for word in question.split() if word in list(df[self.get_info()])]
            
            if not keywords:
                return f"Sorry :(\nNo matching keywords found for your query in {self.get_info()}. More will be added soon\n"
            
            # Find the first matching keyword's response
            responses = [
                list(df[self.get_info() + "_response"])[list(df[self.get_info()]).index(keyword)]
                for keyword in keywords
            ]
            
            # Combine responses if multiple keywords match
            return f" --> {' and '.join(responses)}\n"
        except Exception as e:
            return f"An unexpected error occurred: {e}"


def validate_input(info, user_input):
    """
        Validates user input based on the info type.

        INSTEAD OF HAVING MULTIPLE FUNCTIONS TO VERIFY EACH INPUT
        ---- WE JUST NEEDED TO VERIFY THE SPECIAL FIELDS (EMAIL, BIRTH DATE, GPA AND ENTRY TERM).
        ---- THE REMAINING FIELDS ARE MEANT TO BE STRINGS AS IT STANDS
    """
    if info == "email":
        if "@" not in user_input or "." not in user_input:
            return False, "Invalid email format. Please include '@' and a domain (e.g., example@gmail.com)."
    
    if info == "birth_date":
        try:
            if user_input == 8:
                datetime.strptime(user_input, "%m%d%Y")
        except ValueError:
            return False, "Invalid date format. Please use MMDDYYYY (e.g., 12252000 for Dec 25, 2000)."
    
    if info == "gpa":
        try:
            gpa = float(user_input)
            if gpa < 0.0 or gpa > 4.0:
                return False, "GPA must be a number between 0.0 and 4.0."
        except ValueError:
            return False, "GPA must be a valid number between 0.0 and 4.0."
    
    if info == "entry_term":
        if user_input.lower() not in ["fall", "spring", "summer", "winter"]:
            return False, "Entry term must be either 'fall' or 'spring'."
    
    #returns TRUE if it is not a special field. return True, "" -> returns a tuple!!! That is why it is like this do not interfere
    return True, ""


def main():
    application = {}  # Dictionary to store user inputs 
    
    for info in info_track.keys():
        while True:
            try:
                var = input(f"Please enter your {' '.join(info.split('_'))} here, or type 'help' for assistance: ").strip()
                
                if var.lower() == 'help':
                    # Provides a list of keywords for each
                    print(Berg_Bot(info).lookUp_keyword()) 
                elif var == '':
                    print("Error: This field cannot be empty. Please provide a valid input.")
                else:
                    # Validate input
                    validate, e = validate_input(info, var)
                    if not validate:
                        print(f"Error: {e}")
                    else:
                        application[info] = var  # Saves user input to application dictionary. first_name will be what the user entered
                        break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    
    # Application review and confirmation
    while True:
        try:
            print("\n--- Application Preview ---")
            for key, value in application.items():
                print(f"{' '.join(key.split('_')).upper()}: {value}")
            
            review = input("\nIs the information above correct? (yes/no): ").strip().lower()

            #If the user is done with the application, submit it (It's not going anywhere)
            if review == 'yes':
                print("\nApplication submitted successfully!") 
                break

            #If the user made an error in the application, edit it
            elif review == 'no':
                field_to_edit = input("Which field would you like to update? (i.e. first_name, last_name, birth_date, email, address, entry_term, major, gpa").strip().lower()
                #Check if what the user typed is a field in our info tracker
                if field_to_edit in application:
                    new_value = input(f"Enter new value for {' '.join(field_to_edit.split('_'))}: ").strip()
                    #If the user inputs a value
                    if new_value:
                        #Check if the input is valid for the special fields
                        validate, e = validate_input(field_to_edit, new_value)
                        if not validate:
                            print(f"Error: {e}")
                        #If input is valid, including special fields, update the field
                        else:
                            application[field_to_edit] = new_value
                            print(f"Updated {field_to_edit} to: {new_value}\n")
                    #If input is empty
                    else:
                        print("Values cannot be empty. No changes were made.")
                #If the user input is not in our tracker, do nothing and give an error
                else:
                    print(f"Invalid field: {field_to_edit}. Please try again.")
            #If the user did not enter one of our sentinel values
            else:
                print("Please enter 'yes' or 'no'.")
        #If something goes wrong that we didn't handle. Handle what we didn't handle
        except Exception as e:
            print(f"An unexpected error occurred during review: {e}")
            
    return

if __name__ == '__main__':
        main()
    
