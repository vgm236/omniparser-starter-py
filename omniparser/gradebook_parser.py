#gradebook_parser.py

import os
import pandas
import statistics
import json

#
# CSV VERSION
#

def calculate_average_grade_from_csv(my_csv_filepath):
    
    # Uses the panda package to process the csv (df = dataframe, a special data type from the panda package)
    df = pandas.read_csv(my_csv_filepath)
    avg_grade = df["final_grade"].mean
    # instead of all functions from rows to avg_grade

    # For this specific type of function, "records" is something that allow you to interact with whatever is inside the file
    #rows = df.to_dict("records")
    # Create a list of the grades that were in the file
    #grades = [r["final_grade"] for r in rows]
    # Average out the list
    #avg_grade = statistics.mean(grades)
    
    # Returns what you want for the defined function
    return avg_grade
  
    # This is used when the program is invoke from the command line
if __name__ == "__main__": 
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    # Opens the file. The "__file__" is a reference to the worksheet. We can used cd here as well
    # Os.path.dirname gets the directory name as well - leading to the file you care about
    # You need the "data" and "gradebook" to find it correctly
  
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv") 

    print(gradebook_filepath)

    avg = calculate_average_grade_from_csv(gradebook_filepath)

    print(avg)


#
# JSON VERSION
#

def calculate_average_grade_from_json(my_json_filepath):
    
    #Function to open json file and read it
    with open(my_json_filepath, "r") as f:
        file_contents = f.read()
    # Indentify the list
    gradebook = json.loads(file_contents)
    # Create a list of dictionaries of the students data
    students = gradebook["students"]
    # Create a list of grades from the student data
    grades = [s["finalGrade"] for s in students]
    # Do the average
    avg_grade = statistics.mean(grades)
    return avg_grade



if __name__ == "__main__": 

    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
  
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.json") 

    print(gradebook_filepath)
    #print(os.path.isfile(gradebook_filepath)) # Must show "True"

    avg = calculate_average_grade_from_json(gradebook_filepath)

    print(avg)