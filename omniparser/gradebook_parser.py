#gradebook_parser.py

import os
import pandas as pd
import statistics


def calculate_average_grade_from_csv(my_csv_filepath):
    raw_data = pandas.read_csv(my_csv_filepath)

    rows = df.to_dict("records")
    grades = _________
    avg_grade = statistics.mean(grades)

    return 90.64
    



if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")


    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

    avg = calculate_average_grade_from_csv(gradebook_filepath)

    print(avg)