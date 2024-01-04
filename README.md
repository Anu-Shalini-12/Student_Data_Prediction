# Student_Data_Prediction
# Student Performance Prediction

This project focuses on predicting student performance using logistic regression. The dataset used in this project contains information about students such as gender, race/ethnicity, parental level of education, lunch, test preparation course, math score, reading score, and writing score.

## Table of Contents

- [Libraries Used](#libraries-used)
- [Dataset](#dataset)
- [Steps to Run](#steps-to-run)
- [Necessities](#necessities)

## Libraries Used

The following Python libraries are used in this project:

- [pandas](https://pandas.pydata.org/) - Data manipulation and analysis.
- [scikit-learn](https://scikit-learn.org/) - Machine learning library for logistic regression and model evaluation.

## Dataset

The dataset used in this project is stored in the file `StudentsPerformance.csv` and contains the following columns:

- gender
- race/ethnicity
- parental level of education
- lunch
- test preparation course
- math score
- reading score
- writing score

A new binary target column, `pass_fail`, is created based on the sum of math, reading, and writing scores.

## Steps to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/Anu-Shalini-12/Student_Data_Prediction
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the `Data_prediction` script:

    ```bash
    python Data_prediction.py
    ```

4. Check the updated dataset in the file `StudentsPerformance_updated.csv`.

## Additional Notes

- **CSV File Path:**
  - Ensure that the CSV file path in `file_path` is correct.

## Necessities

- Python 3.x
- pip (Python package installer)

Ensure that you have Python installed on your machine and that the required libraries are installed using the provided `requirements.txt` file.

## Author

Anu-Shalini-12
