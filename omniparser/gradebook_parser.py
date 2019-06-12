#gradebook_parser.py

import os
import pandas
import statistics


def calculate_average_grade_from_csv(my_csv_filepath):
# Uses the panda package to process the csv (df = dataframe, a special data type from the panda package)
    df = pandas.read_csv(my_csv_filepath)
# For this specific type of function, "records" is something that allow you to interact with whatever is inside the file
    rows = df.to_dict("records")
# Create a list of the grades that were in the file
    grades = [r["final_grade"] for r in rows]
# Average out the list
    avg_grade = statistics.mean(grades)
    # or avg_grade = df["final_grade"].mean


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